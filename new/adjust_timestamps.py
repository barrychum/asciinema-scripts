import json
import sys

def adjust_timestamps(input_file, output_file, start_time, max_interval):
    with open(input_file, 'r') as f:
        # Read and parse the header
        header = json.loads(f.readline())
        
        # Read all events
        events = [json.loads(line) for line in f]

    # Adjust timestamps
    first_timestamp = events[0][0]
    for event in events:
        # Shift all timestamps by start_time and subtract the first timestamp
        event[0] = start_time + (event[0] - first_timestamp)

    # Adjust intervals
    for i in range(1, len(events)):
        interval = events[i][0] - events[i-1][0]
        if interval > max_interval:
            # Format the adjusted timestamp with f-string
            adjusted_timestamp = f"{events[i-1][0] + max_interval:.6f}"
            events[i][0] = float(adjusted_timestamp)  # Convert back to float

    # Write adjusted data to output file
    with open(output_file, 'w') as f:
        json.dump(header, f)
        f.write('\n')
        for event in events:
            json.dump(event, f)
            f.write('\n')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py input.cast output.cast start_time max_interval")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_time = float(sys.argv[3])
    max_interval = float(sys.argv[4])

    adjust_timestamps(input_file, output_file, start_time, max_interval)
    print(f"Adjusted to start at {start_time} second")
    print(f"with a maximum interval of {max_interval} seconds betwen keystrokes.")
