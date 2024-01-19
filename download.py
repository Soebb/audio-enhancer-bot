# init
output = 'martinreel1v1_enhanced'
output_path = "/Volumes/My Passport/draft/martinreel1v1_enhanced.mp3" 
 
import requests
import json 

APP_KEY = '30VDYtAvTUo_hFXC-rJgbQ=='  # replace abc with your actual app key
APP_SECRET = 'PLsFemvYtizbl84KmrSpxUxu1q4HELdBd2gufycnxfg='  # replace xyz with your actual secret key

payload = { 'grant_type': 'client_credentials', 'expires_in': 1800 }
response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
body = json.loads(response.content)
api_token = body['access_token']


import os
import shutil
import requests



url = "https://api.dolby.com/media/output"
headers = {
    "Authorization": "Bearer {0}".format(api_token),
    "Content-Type": "application/json",
    "Accept": "application/json"
}

args = {
    "url": f"dlb://out/{output}.mp3",
}

with requests.get(url, params=args, headers=headers, stream=True) as response:
    response.raise_for_status()
    response.raw.decode_content = True
    print("Downloading from {0} into {1}".format(response.url, output_path))
    with open(output_path, "wb") as output_file:
        shutil.copyfileobj(response.raw, output_file)
