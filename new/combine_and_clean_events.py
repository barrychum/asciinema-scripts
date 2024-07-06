import json
import sys

def read_asciinema_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    try:
        # Try to parse the entire file as a single JSON object
        return json.loads(''.join(lines))
    except json.JSONDecodeError:
        # If that fails, try to parse each line as a separate JSON object
        try:
            data = [json.loads(line.strip()) for line in lines if line.strip()]
            if data and isinstance(data[0], dict) and 'version' in data[0]:
                # The first object is likely the header
                return data
            else:
                # If no header is found, assume it's just a list of events
                return [{'version': 2, 'width': 80, 'height': 24}] + data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

def combine_and_clean_events(input_file, output_file, min_interval):
    data = read_asciinema_file(input_file)
    if data is None:
        print("Failed to read the input file.")
        return

    # Extract the header and events
    if isinstance(data[0], dict) and 'version' in data[0]:
        header = data[0]
        events = data[1:]
    else:
        header = {'version': 2, 'width': 80, 'height': 24}
        events = data

    # Process events
    new_events = []
    current_output = ""
    current_time = 0
    
    for event in events:
        time, event_type, content = event
        
        if event_type == "o":  # Output event
            if new_events and time < min_interval:
                # Combine with previous event if interval is small
                new_events[-1][0] += time
                new_events[-1][2] += content
            else:
                new_events.append([time, event_type, content])
            current_time += time
        
        elif event_type == "i":  # Input event
            if content == "\b":  # Backspace
                if current_output:
                    current_output = current_output[:-1]
            else:
                current_output += content
            
            # Add accumulated input as a new event
            if new_events and new_events[-1][1] == "i":
                new_events[-1][2] = current_output
            else:
                new_events.append([time, event_type, current_output])
            current_time += time
    
    # Update the duration in the header
    header['duration'] = current_time
    
    # Write the modified data to the output file
    with open(output_file, 'w') as f:
        json.dump([header] + new_events, f)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py input_file output_file min_interval")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    min_interval = float(sys.argv[3])
    
    combine_and_clean_events(input_file, output_file, min_interval)
    print(f"Events processed. Minimum interval: {min_interval} seconds.")