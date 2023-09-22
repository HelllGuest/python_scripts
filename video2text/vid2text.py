import argparse
import moviepy.editor as mp
import speech_recognition as sr
import os
import logging

# Function to validate file existence
def validate_file_existence(file_path):
    if not os.path.isfile(file_path):
        logging.error(f"File not found: {file_path}")
        return False
    return True

# Function to perform audio transcription
def transcribe_audio(video_name, output_name, output_format='txt', verbose=False):
    try:
        # Load the video
        video_path = os.path.abspath(video_name)
        if not validate_file_existence(video_path):
            return

        video = mp.VideoFileClip(video_path)

        if verbose:
            print("Video loaded successfully.")

        # Extract audio
        audio = video.audio

        if verbose:
            print("Audio extracted successfully.")

        # Write audio to temp wav file
        temp = "temp.wav"
        audio.write_audiofile(temp)

        if verbose:
            print("Audio written to temp file successfully.")

        # Transcribe audio
        r = sr.Recognizer()
        with sr.AudioFile(temp) as source:
            audio_text = r.listen(source)
            try:
                text = r.recognize_google(audio_text)
            except sr.UnknownValueError:
                logging.error("Google Speech Recognition could not understand audio")
                text = ""
            except sr.RequestError as e:
                logging.error(f"Could not request results from Google Speech Recognition service; {e}")
                text = ""

        # Delete temp file
        os.remove(temp)

        if verbose:
            print("Temp file deleted successfully.")

        # Save transcript to user specified text file
        with open(output_name, mode="w") as file:
            file.write(text)

        if output_format == 'txt':
            print("Transcript saved as a text file.")
        elif output_format == 'json':
            import json
            with open(output_name, mode="w") as file:
                json.dump({'transcript': text}, file)
            print("Transcript saved as a JSON file.")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Set up logging
logging.basicConfig(filename='transcribe.log', level=logging.ERROR)

# Create a command-line argument parser
parser = argparse.ArgumentParser(description="Transcribe audio from a video.")

# Define command-line arguments
parser.add_argument("video_name", help="Enter video file name (relative or absolute path)")
parser.add_argument("output_name", help="Enter output file name")
parser.add_argument("--output_format", default="txt", choices=["txt", "json"], help="Enter output format (txt or json)")
parser.add_argument("--verbose", "-v", action="store_true", help="Display detailed process information")

# Parse command-line arguments
args = parser.parse_args()

# Call the transcribe_audio function with the provided arguments
transcribe_audio(args.video_name, args.output_name, args.output_format, args.verbose)
