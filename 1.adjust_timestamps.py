import json
import sys

def adjust_timestamps(input_file, output_file, start_time, max_interval):
    with open(input_file, 'r') as f:
        # Read and parse the header
        header = json.loads(f.readline())
        
        # Read all events
        events = [json.loads(line) for line in f]

    new_events = []
    temp_event = []

   # Adjust start time
    temp_event = [element for element in events[0]]
    temp_event[0] = start_time
    new_events.append(temp_event)

    # Adjust intervals
    for i in range(1, len(events)):
        temp_event = [element for element in events[i]]
        interval = events[i][0] - events[i-1][0]

        break_interval = 1.0
        if temp_event[2] == "\b  " :
            temp_event[0] = new_events[i-1][0] + break_interval
        else:
            if interval > max_interval:
                temp_event[0] = new_events[i-1][0] + max_interval
            else:
                temp_event[0] = new_events[i-1][0] + interval

        # Format the adjusted timestamp with f-string
        adjusted_timestamp = f"{temp_event[0]:.6f}"
        temp_event[0] = float(adjusted_timestamp)  # Convert back to float

        new_events.append(temp_event)

    # Write adjusted data to output file
    with open(output_file, 'w') as f:
        json.dump(header, f)
        f.write('\n')
        for event in new_events:
            json.dump(event, f)
            f.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 1.adjust_timestamps.py input.cast output.cast start_time max_interval")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_time = float(sys.argv[3])
    max_interval = float(sys.argv[4])

    adjust_timestamps(input_file, output_file, start_time, max_interval)
    print(f"Adjusted to start at {start_time} second")
    print(f"with a maximum interval of {max_interval} seconds betwen keystrokes.")
