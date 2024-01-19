import os
import requests
import json
from dotenv import load_dotenv
from store import upload_audio
from enhance import enhance_audio
from download import download_audio

class AudioProcessing:
    def __init__(self, input_path, input_name, output_name, output_path):
        load_dotenv()
        self.input_path = input_path
        self.input_name = input_name
        self.output_name = output_name
        self.output_path = output_path

    def run(self):
        upload_audio(self.input_path, self.input_name)
        enhance_audio(self.input_name, self.output_name)
        download_audio(self.output_name, self.output_path)

# Usage example:
if __name__ == "__main__":
    input_path = ""  # Set your input file location
    input_name = ''  # Set your input file name
    output_name = ''  # Set your output file name
    output_path = ''  # Set your output file location

    audio_processor = AudioProcessing(input_path, input_name, output_name, output_path)
    audio_processor.run()
