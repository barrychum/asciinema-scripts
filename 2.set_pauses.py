#!/usr/bin/env python3

import json
import sys

def adjust_pause(input_file, output_file, pause):
    with open(input_file, 'r') as f:
        # Read and parse the header
        header = json.loads(f.readline())
        
        # Read all events
        events = [json.loads(line) for line in f]

    new_events = []
    temp_event = []

    temp_event = [element for element in events[0]]
    new_events.append(temp_event)

    adjustment = 0.0
    
    # Adjust intervals
    for i in range(1, len(events)):
        temp_event = [element for element in events[i]]

        if temp_event[2] == "\b  " :
            adjustment = pause - (events[i][0] - new_events[i-1][0])
            temp_event[0] = temp_event[0] + adjustment
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

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 2.set_pauses.py input.cast output.cast pause")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    pause = float(sys.argv[3])

    adjust_pause(input_file, output_file, pause)

