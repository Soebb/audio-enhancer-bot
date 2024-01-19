#init
# give input file name and output file name
input_name = '' # name of stored cloud file - from store.py
output_name = '' # set name of enhanced cloud file

# get access token
import requests
import json
from dotenv import load_dotenv

load_dotenv()


APP_KEY = os.getenv("DOLBY_AUDIO_KEY")  # replace abc with your actual app key
APP_SECRET = os.getenv("DOLBY_API_KEY")  # replace xyz with your actual secret key

payload = { 'grant_type': 'client_credentials', 'expires_in': 1800 }
response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
api_token = body['access_token']

#https://docs.dolby.io/media-apis/reference/media-enhance-post
import os
import requests

# Set or replace these values
body = {
  "input" : f"dlb://in/{input_name}.mp3",
  "output" : f"dlb://out/{output_name}.mp3",
  "content" : {
      "type": "voice_recording" # change to phone
  },
    "audio": {
        "noise":{
          "reduction":{
              "enable": True
          }  
        },
        "loudness": {
            "enable": True, 
            "dialog_intelligence": True 
            },
        "filter": {
            "dynamic_eq": { "enable": True },
            "high_pass": { "enable": True },
            "hum": { "enable": True }
        },
        "speech": {
            "isolation": { "enable": True } # , "amount": 25 }   
        }
    }
}


url = "https://api.dolby.com/media/enhance"
headers = {
    "Authorization": "Bearer {0}".format(api_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, json=body, headers=headers)
response.raise_for_status()
print(response.json())
