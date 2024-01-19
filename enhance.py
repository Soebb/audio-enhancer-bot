#init
input = 'martinreel1v1'
output = 'martinreel1v1_enhanced'

# get access token

import requests
import json

APP_KEY = '30VDYtAvTUo_hFXC-rJgbQ=='  # replace abc with your actual app key
APP_SECRET = 'PLsFemvYtizbl84KmrSpxUxu1q4HELdBd2gufycnxfg='  # replace xyz with your actual secret key

payload = { 'grant_type': 'client_credentials', 'expires_in': 1800 }
response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
api_token = body['access_token']

#https://docs.dolby.io/media-apis/reference/media-enhance-post
import os
import requests

# Set or replace these values
body = {
  "input" : f"dlb://in/{input}.mp3",
  "output" : f"dlb://out/{output}.mp3",
  "content" : {
      "type": "voice_recording"
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
