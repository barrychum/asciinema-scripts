# asciinema scripts

This repository contains scripts for working with asciinema recordings, specifically for modifying recorded pauses and converting cast files to SVG.

## Features

- Adjust pauses in asciinema cast files to a maximum specified duration.
- Set a specific start time for the first event.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/barrychum/asciinema-scripts.git
    cd asciinema-scripts
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Adjust the `first_event_start` variable:

    Open `trim_pauses.py` in your preferred text editor and set the `first_event_start` variable at the beginning of the script to your desired start time in seconds. Set it to `0` to keep the original timestamp of the first event.

    ```python
    # Define the variable to set the starting timestamp for the first event
    first_event_start = 0  # Set this to the desired start time in seconds, or 0 to keep the original timestamp
    ```

2. Run the script:

    ```sh
    python trim_pauses.py /path/to/your.cast
    ```

    This will produce a new file with the adjusted pauses, saved as `<original_filename>_trimmed.cast` in the same directory as the input file.

## Example

Suppose you have a cast file named `example.cast` and you want to set the start time of the first event to `0.5` seconds and ensure no pause exceeds `0.5` seconds. Set the `first_event_start` variable to `0.5` in the script:

```python
first_event_start = 0.5
```

Then run the script:

```sh
python trim_pauses.py example.cast
```

The output file `example_trimmed.cast` will have the adjusted timestamps.

## Basic asciinema Operations

### Recording a Terminal Session

To record a terminal session:

```sh
asciinema rec
```

This starts recording your terminal session. To finish and save the recording, press `Ctrl-D` or type `exit`.

### Playing a Recording

To play a recording:

```sh
asciinema play /path/to/your.cast
```

### Playing a Recording in Loop Mode

To play a recording in a loop:

```sh
asciinema play -l /path/to/your.cast
```

### Playing a Recording with Idle Time Limit

To play a recording with an idle time limit:

```sh
asciinema play -l --idle-time-limit=0.5 /path/to/your.cast
```

This will limit the idle time between commands to 0.5 seconds.

<img src="assets/output.svg" width="800" alt="Animated SVG">

## Docker Integration for SVG Conversion

You can use Docker to convert the cast file generated in this repository to an SVG file.

### Dockerfile

```Dockerfile
FROM node:14-alpine

# Install dependencies
RUN apk add --no-cache git python3 make g++ && \
    npm install -g svg-term-cli && \
    apk del git python3 make g++

# Set the working directory
WORKDIR /usr/src/app

# Entrypoint to pass arguments
ENTRYPOINT ["svg-term"]
```

### Steps to Build and Run the Docker Container

1. **Create a Dockerfile:**

    Save the updated Dockerfile content to a file named `Dockerfile`.

2. **Build the Docker Image:**

    Open a terminal, navigate to the directory containing the Dockerfile, and run the following command to build the Docker image:

    ```sh
    docker build -t svg-term-converter .
    ```

3. **Run the Docker Container with Arguments:**

    Run the following command to convert the input cast file to an output SVG file by specifying the filenames:

    ```sh
    docker run --rm -v $(pwd):/usr/src/app svg-term-converter --in input.cast --out output.svg
    ```

### Example Commands

Here’s a sequence of commands to create the Dockerfile, build the image, and run the container with specified filenames:

```sh
# Step 1: Create a Dockerfile
cat <<EOF > Dockerfile
FROM node:14-alpine

# Install dependencies
RUN apk add --no-cache git python3 make g++ && \
    npm install -g svg-term-cli && \
    apk del git python3 make g++

# Set the working directory
WORKDIR /usr/src/app

# Entrypoint to pass arguments
ENTRYPOINT ["svg-term"]
EOF

# Step 2: Build the Docker image
docker build -t svg-term-converter .

# Step 3: Ensure the input cast file is in the current directory
# Step 4: Run the Docker container to perform the conversion with specified filenames
docker run --rm -v $(pwd):/usr/src/app svg-term-converter --in input.cast --out output.svg

# The output.svg should now be in the current directory
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [asciinema](https://asciinema.org) team for creating such a useful tool.



