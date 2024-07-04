# Audio channel splitter

## Description

**audio_channel_splitter** is a Python tool that splits stereo audio files into `separate left and right channel` files. It supports various audio formats such as `WAV`, `MP3`, and `FLAC` using the Pydub library.

## Features

- Split stereo audio files into separate left and right channels.
- Supports multiple audio formats: WAV, MP3, FLAC.
- Automatically appends "_left" and "_right" to the original file name.
- Lightweight and easy to use.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/audio_channel_splitter.git
    cd audio_channel_splitter
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place your stereo audio file in the project directory.**

2. **Run the script:**

    ```bash
    python audio_channel_splitter.py
    ```

    **Example:**

    ```python
    input_file = "a.wav"  # Replace with your actual file name and format
    split_stereo_to_mono(input_file)
    ```

3. **Output:**

    The script will generate two new files in the same directory:
    - a_left.wav
    - a_right.wav

## License

This project is licensed under the `MIT` License.
