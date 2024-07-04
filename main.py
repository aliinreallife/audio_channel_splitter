from pydub import AudioSegment
import os


def split_stereo_to_mono(input_file: str) -> tuple[AudioSegment, AudioSegment]:
    """
    Split a stereo audio file into two mono audio segments, one for the left channel and one for the right channel.
    The function returns the mono segments for further processing.

    Args:
        input_file (str): Path to the stereo audio file.

    Returns:
        tuple[AudioSegment, AudioSegment]: A tuple containing two AudioSegment objects,
                                           the first for the left channel and the second for the right channel.

    Raises:
        ValueError: If the input file format is not supported.
        ValueError: If the input file is not a two-channel stereo audio file.
    """
    supported_formats = [".wav", ".mp3", ".flac"]
    file_extension = os.path.splitext(input_file)[1].lower()
    if file_extension not in supported_formats:
        raise ValueError(
            f"Unsupported file format: {file_extension}. Supported formats are {supported_formats}"
        )

    audio = AudioSegment.from_file(input_file)

    if audio.channels == 1:
        raise ValueError(
            "The input file is already a mono audio file and cannot be split into stereo channels."
        )
    elif audio.channels != 2:
        raise ValueError("The input file is not a stereo audio file.")

    right_channel, left_channel = audio.split_to_mono()

    return left_channel, right_channel


# Usage example with export functionality
if __name__ == "__main__":

    input_file = "a.mp3"  # Replace with your actual file name and format

    left_channel, right_channel = split_stereo_to_mono(input_file)

    # Construct output file paths
    base_name, ext = os.path.splitext(input_file)
    ext = ext[1:]  # Remove the leading dot

    # Check if the format is supported for export
    if ext not in ["wav", "mp3", "flac"]:
        raise ValueError(f"The format '{ext}' is not supported for export.")

    left_channel_file = f"{base_name}_left.{ext}"
    right_channel_file = f"{base_name}_right.{ext}"

    # Export the mono channels using the extracted format
    left_channel.export(left_channel_file, format=ext)
    right_channel.export(right_channel_file, format=ext)

    print(f"Left channel saved to: {left_channel_file}")
    print(f"Right channel saved to: {right_channel_file}")
