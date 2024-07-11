# asciinema scripts

asciinema is an excellent light weight terminal recoding software.  This repository contains scripts for working with asciinema recordings, specifically for modifying recorded pauses and converting cast files to SVG.

## Features

- Adjust pauses in asciinema cast files to a maximum specified duration.
- Set a specific start time for the first event.

## asciinema quick start

```
# example
asciinema rec --command "/usr/local/bin/bash --rcfile /Users/user/.bash5profile -i" --idle-time-limit 2 --quiet --overwrite test.cast
```

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/barrychum/asciinema-scripts.git
    cd asciinema-scripts
    ```

## Usage


#### Extract a section of the video
```
python 0.extract_cast.py input_file output_file <start in seconds> <end in seconds>
```

#### Adjust the start time and maximum interval
```
python 1.adjust_timestamps.py input.cast output.cast start_time max_interval
```

#### Insert a delay
```
python 2.insert_delay.py input_file output_file <time in seconds> delay
```

#### Set an interval 
```
python 2.set_delay.py input_file output_file <time in seconds> delay
```

#### Set pause interval (undocumented feature)

`Note`: I noticed the recorded cast file has a special sequence "\b  " when you press spacebar twice.  I wrote a script to detect this key sequence and set the interval.  This function may break.  

```
python 2.set_pauses.py input.cast output.cast <pause in seconds>
```
  

  
  
## Basic asciinema Operations

### Recording a Terminal Session

To record a terminal session:

```sh
asciinema rec
```

This starts recording your terminal session. To finish and save the recording, press `Ctrl-D` or type `exit`.

To pause and resume recording (e.g. to enter password), press `Ctrl-\`.

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

<!--
<img src="assets/output.svg" width="800" alt="Animated SVG">
-->

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
FROM node:20-alpine

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

docker run --rm -v $(pwd):/usr/src/app svg-term-converter --in input.cast --out output.svg --width 80 --height 24


# The output.svg should now be in the current directory
```


<img src="__test__/output.svg" width="400" height="300">

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [asciinema](https://asciinema.org) team for creating such a useful tool.



