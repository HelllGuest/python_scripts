# Video to Audio Transcript

This Python script allows you to transcribe the audio from a video file and save the transcript to a text or JSON file. It uses the MoviePy library to process the video and the SpeechRecognition library for audio transcription.

## Dependencies

Install required libraries:

```
pip install moviepy
pip install speechrecognition
```

You will also need [FFmpeg](https://ffmpeg.org/download.html) installed for moviepy to work.

## Usage

```bash
python vid2text.py [video_name] [output_name] [--output_format {txt,json}] [--verbose]
```

Replace the placeholders with your specific inputs:
- `[video_name]`: Enter the name of the video file you want to transcribe. You can provide a relative or absolute path.
- `[output_name]`: Enter the desired name of the output file where the transcript will be saved.
- `[--output_format {txt,json}]` (optional): Specify the output format as either "txt" or "json." If not provided, it defaults to "txt."
- `[--verbose]` (optional): Use this flag to enable detailed process information during execution.

4. The script will process the video, transcribe the audio, and save the transcript to the specified output file.

## Example Usage

Here's an example of how to use the script:
```bash
vid2text.py D:\video\1.mp4 22.txt --output_format json
```

## Script Overview

The script does the following:

- Loads the video using moviepy
- Extracts the audio track 
- Writes audio to a temp wav file
- Transcribes audio using SpeechRecognition API 
- Deletes temp audio file
- Saves transcribed text to output file

## Troubleshooting

Errors to check for:

- Module not found - install dependencies
- FFmpeg not found - install FFmpeg
- Audio could not be transcribed - improve audio quality
- Invalid file name - check video file path

## Error Handling

If the script encounters errors during the transcription process, it will log them in a file named transcribe.log for debugging and monitoring purposes. You can check this log file for any issues that may arise.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as you wish.
