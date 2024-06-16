# Asciinema Pause Trimmer

A Python script to adjust pauses in Asciinema cast files, ensuring no pause exceeds a specified maximum duration. The script also allows setting a specific start time for the first event.

## Features

- Adjusts pauses in Asciinema cast files to a maximum specified duration.
- Allows setting a specific start time for the first event.
- Formats timestamps to exactly 6 decimal places without quotes.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/asciinema-pause-trimmer.git
    cd asciinema-pause-trimmer
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Adjust the `first_event_start` variable:**

   Open `trim_pauses.py` in your preferred text editor and set the `first_event_start` variable at the beginning of the script to your desired start time in seconds. Set it to `0` to keep the original timestamp of the first event.

   ```python
   # Define the variable to set the starting timestamp for the first event
   first_event_start = 0  # Set this to the desired start time in seconds, or 0 to keep the original timestamp
   ```

2. **Run the script:**

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

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the [Asciinema](https://asciinema.org) team for creating such a useful tool.