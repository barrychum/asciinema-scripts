#!/usr/bin/env python3

import json
import sys

def insert_delay(input_file, output_file, timestamp, delay):
    with open(input_file, 'r') as f:
        # Read and parse the header
        header = json.loads(f.readline())
        
        # Read all events
        events = [json.loads(line) for line in f]

    inserted = False

    new_events = []
    temp_event = []

   # Adjust start time
    temp_event = [element for element in events[0]]
    new_events.append(temp_event)

    # Adjust intervals
    for i in range(1, len(events)):
        temp_event = [element for element in events[i]]
        if not inserted:
            if events[i][0] > timestamp :
                inserted = True
                temp_event[0] = temp_event[0] + delay
                adjusted_timestamp = f"{temp_event[0]:.6f}"
                temp_event[0] = float(adjusted_timestamp)
        else:
            temp_event[0] = temp_event[0] + delay
            adjusted_timestamp = f"{temp_event[0]:.6f}"
            temp_event[0] = float(adjusted_timestamp)
        new_events.append(temp_event)

    # Write adjusted data to output file
    with open(output_file, 'w') as f:
        json.dump(header, f)
        f.write('\n')
        for event in new_events:
            json.dump(event, f)
            f.write('\n')

    if inserted:
        print(f"Inserted {delay} seconds at {timestamp} second")
    else:
        print(f"Clip shorted than the provided timestamp")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 2.insert_delay.py input_file output_file timestamp delay")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    timestamp = float(sys.argv[3])
    delay = float(sys.argv[4])

    insert_delay(input_file, output_file, timestamp, delay)

