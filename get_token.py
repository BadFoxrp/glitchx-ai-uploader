from google_auth_oauthlib.flow import InstalledAppFlow
import os
import json

# Nustatyk reikiamas teisės (scopes)
scopes = ["https://www.googleapis.com/auth/youtube.upload"]

# Paleisk autentifikavimo srautą
flow = InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", scopes=scopes
)
creds = flow.run_local_server(port=0)

# Išsaugok token.json
with open("token.json", "w") as token_file:
    token_file.write(creds.to_json())

print("✅ token.json failas sukurtas")
