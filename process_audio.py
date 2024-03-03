import os
import requests
import json
from store import upload_audio
from enhance import enhance_audio
from download import download_audio

class AudioProcessing:
    def __init__(self, input_path, input_name, output_name, output_path):
        self.input_path = input_path
        self.input_name = input_name
        self.output_name = output_name
        self.output_path = output_path

    def run(self):
        upload_audio(self.input_path, self.input_name)
        enhance_audio(self.input_name, self.output_name)
        download_audio(self.output_name, self.output_path)
