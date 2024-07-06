import json
import sys

def extract(input_file, output_file, start, end):
    with open(input_file, 'r') as f:
        # Read and parse the header
        header = json.loads(f.readline())
        
        # Read all events
        events = [json.loads(line) for line in f]

    new_events = []
    temp_event = []
    
    # Adjust intervals
    for i in range(0, len(events)):
        if events[i][0] >= start and events[i][0] <= end:
            temp_event = [element for element in events[i]]
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
        print("Usage: python insert_delay.py input_file output_file timestamp delay")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start = float(sys.argv[3])
    end = float(sys.argv[4])

    extract(input_file, output_file, start, end)

