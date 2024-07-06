import json
import sys

def insert_delay(input_file, output_file, timestamp, delay):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # Parse the header and events
    header = json.loads(lines[0])
    events = [json.loads(line) for line in lines[1:] if line.strip()]
    
    # Insert the delay
    new_events = []
    total_time = 0
    for event in events:
        if total_time >= timestamp:
            # Insert delay event
            new_events.append([delay, "o", ""])
            # Adjust all subsequent timestamps
            event[0] += delay
        new_events.append(event)
        total_time += event[0]
    
    # Calculate total duration
    total_duration = sum(event[0] for event in new_events)
    
    # Update or add the duration in the header
    if 'duration' in header:
        header['duration'] = total_duration
    else:
        header['duration'] = total_duration
    
    # Write the modified data to the output file
    with open(output_file, 'w') as f:
        f.write(json.dumps(header) + '\n')
        for event in new_events:
            f.write(json.dumps(event) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python insert_delay.py input_file output_file timestamp delay")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    timestamp = float(sys.argv[3])
    delay = float(sys.argv[4])
    
    insert_delay(input_file, output_file, timestamp, delay)
    print(f"Delay of {delay} seconds inserted at {timestamp} seconds.")