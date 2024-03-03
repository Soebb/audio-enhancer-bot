import os
import requests
import json


def upload_audio(input_path, input_name):
    APP_KEY = os.environ.get("API_KEY")  # Replace with your actual app key
    APP_SECRET = os.environ.get("API_SECRET")  # Replace with your actual secret key

    payload = {'grant_type': 'client_credentials', 'expires_in': 1800}
    response = requests.post('https://api.dolby.io/v1/auth/token', data=payload, auth=requests.auth.HTTPBasicAuth(APP_KEY, APP_SECRET))
    body = json.loads(response.content)
    api_token = body['access_token']

    # Declare your dlb:// location
    url = "https://api.dolby.com/media/input"
    headers = {
        "Authorization": "Bearer {0}".format(api_token),
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    body = {
        "url": f"dlb://{input_name}.mp3",
    }

    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    data = response.json()
    presigned_url = data["url"]

    # Upload your media to the pre-signed url response
    print("Uploading {0} to {1}".format(input_path, presigned_url))
    with open(input_path, "rb") as input_file:
        requests.put(presigned_url, data=input_file)

# Usage example:
#upload_audio(input_path, input_name)
