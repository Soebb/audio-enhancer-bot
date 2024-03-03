import os
import requests
import json

def enhance_audio(input_name, output_name):
    APP_KEY = os.environ.get("API_KEY")  # Replace with your actual app key
    APP_SECRET = os.environ.get("API_SECRET")  # Replace with your actual secret key

    payload = {'grant_type': 'client_credentials', 'expires_in': 1800}
    response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
    body = json.loads(response.content)
    api_token = body['access_token']

    # Set or replace these values
    body = {
        "input" : f"dlb://in/{input_name}.mp3",
        "output" : f"dlb://out/{output_name}.mp3",
        "content" : {
            "type": "mobile_phone"  # change based on recording device - refer to api docs linked in readme
        },
        "audio": {
            "noise": {
                "reduction": {
                    "enable": True
                }
            },
            "loudness": {
                "enable": True, 
                "dialog_intelligence": True
            },
            "filter": {
                "dynamic_eq": {"enable": True},
                "high_pass": {"enable": True},
                "hum": {"enable": True}
            },
            "speech": {
                "isolation": {"enable": True}  # , "amount": 25 }
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

# Usage example:
#enhance_audio(input_name, output_name)
