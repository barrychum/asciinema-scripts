import json
import sys
import os

def adjust_pauses(cast_file, max_pause=0.5):
    events = []
    header = None

    with open(cast_file, 'r') as f:
        lines = f.readlines()

        # Read the first line as the header JSON object
        try:
            header = json.loads(lines[0].strip())
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON header: {e}")
            return

        # Process the remaining lines as individual JSON arrays
        for line in lines[1:]:
            line = line.strip()
            if not line or not line.startswith('['):
                continue
            try:
                event = json.loads(line)
                events.append(event)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON event on line: {line}")
                print(e)
                return

    # Create a list of all original timestamps
    original_timestamps = [event[0] for event in events]

    # Calculate the required adjustments
    adjusted_timestamps = [original_timestamps[0]]  # Start with the first timestamp
    for i in range(1, len(original_timestamps)):
        pause = original_timestamps[i] - original_timestamps[i - 1]
        if pause > max_pause:
            adjusted_timestamps.append(adjusted_timestamps[-1] + max_pause)
        else:
            adjusted_timestamps.append(adjusted_timestamps[-1] + pause)

    # Normalize timestamps only if the first event starts in more than 0.5 seconds
    start_time = adjusted_timestamps[0]
    if start_time > 0.5:
        normalized_timestamps = [round(ts - start_time + 0.5, 6) for ts in adjusted_timestamps]
    else:
        normalized_timestamps = [round(ts, 6) for ts in adjusted_timestamps]

    # Adjust the events with the new timestamps, formatted to 6 decimal places
    adjusted_events = []
    for i, event in enumerate(events):
        formatted_timestamp = round(normalized_timestamps[i], 6)
        adjusted_events.append([formatted_timestamp] + event[1:])

    # Determine the new file name
    base, ext = os.path.splitext(cast_file)
    new_file = base + '_trimmed' + ext

    # Write back the adjusted cast file
    with open(new_file, 'w') as f:
        f.write(json.dumps(header) + '\n')
        for event in adjusted_events:
            # Manually format the event string to ensure the timestamp has 6 decimal places without quotes
            timestamp_str = f'{event[0]:.6f}'
            event_str = json.dumps([timestamp_str] + event[1:])[1:-1]  # Remove the surrounding brackets
            f.write(f'[{timestamp_str}, {event_str.split(",", 1)[1]}]\n')

    print(f"Trimmed cast file saved as: {new_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python trim_pauses.py <path_to_cast_file>")
        sys.exit(1)

    cast_file = sys.argv[1]
    adjust_pauses(cast_file, max_pause=0.5)
