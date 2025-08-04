
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import json

def upload_to_youtube(video_path, title, description):
    # Įkeliame konfigūraciją
    with open("config.json", "r") as f:
        config = json.load(f)

    # Naudojame slapukų failą su iš anksto gautais prisijungimais (OAuth2)
    # Failas credentials.json turi būti gautas per Google Cloud konsolę
    creds = Credentials.from_authorized_user_file("token.json", ["https://www.googleapis.com/auth/youtube.upload"])

    youtube = build("youtube", "v3", credentials=creds)

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["gaming", "GlitchX", "AI", "trending", "FiveM"],
            "categoryId": "20"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Įkėlimo būsena: {int(status.progress() * 100)}%")

    print(f"Sėkmingai įkelta: https://www.youtube.com/watch?v={response['id']}")
