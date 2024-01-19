# init
input_path = "" # file location
input_name = '' # file name when uploaded to dolby cloud

# get access token

import requests
import json

APP_KEY = os.getenv("DOLBY_AUDIO_KEY")  # replace abc with your actual app key
APP_SECRET = os.getenv("DOLBY_API_KEY")  # replace xyz with your actual secret key

payload = { 'grant_type': 'client_credentials', 'expires_in': 1800 }
response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
api_token = body['access_token']


# store audio

import os
import requests

# Declare your dlb:// location

url = "https://api.dolby.com/media/input"
headers = {
    "Authorization": "Bearer {0}".format(api_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

body = {
    "url": f"dlb://in/{input_name}.mp3",
}

response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
data = response.json()
presigned_url = data["url"]

# Upload your media to the pre-signed url response

print("Uploading {0} to {1}".format(input_path, presigned_url))
with open(input_path, "rb") as input_file:
  requests.put(presigned_url, data=input_file)





