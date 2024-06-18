from pydub import AudioSegment
import os

def split_stereo_to_mono(input_file):
    supported_formats = ['.wav', '.mp3', '.flac']
    file_extension = os.path.splitext(input_file)[1].lower()
    if file_extension not in supported_formats:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats are {supported_formats}")

    audio = AudioSegment.from_file(input_file)

    if audio.channels != 2:
        raise ValueError("The input file is not a stereo audio file.")

    left_channel, right_channel = audio.split_to_mono()
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    left_output = f"{base_name}_left{file_extension}"
    right_output = f"{base_name}_right{file_extension}"

    left_channel.export(left_output, format=file_extension[1:])
    print(f"Left channel saved as: {left_output}")

    right_channel.export(right_output, format=file_extension[1:])
    print(f"Right channel saved as: {right_output}")

# Usage example
if __name__ == "__main__":
    input_file = "a.wav"  # Replace with your actual file name and format
    split_stereo_to_mono(input_file)
