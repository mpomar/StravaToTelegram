from config import strava_id, strava_secret, api_id, api_hash, bot_token
import requests
from urllib.parse import urlencode
from pyrogram import Client, filters

# Get authorization code
url = 'https://www.strava.com/api/v3/'
authorization_url = 'https://www.strava.com/oauth/authorize'
redirect_uri = 'http://localhost:8080/callback'
scope = 'read_all,activity:read_all'

authorize_params = {
    'client_id': strava_id,
    'redirect_uri': redirect_uri,
    'response_type': 'code',
    'scope': scope,
}

authorize_url = f'{authorization_url}?{urlencode(authorize_params)}'
print(f'Authorize the app by visiting the following link and copy the authorization code from the URL:\n{authorize_url}')
authorization_code = input('Enter the authorization code from the callback URL: ')

# Get access token
token_url = 'https://www.strava.com/oauth/token'
token_params = {
    'client_id': strava_id,
    'client_secret': strava_secret,
    'code': authorization_code,
    'grant_type': 'authorization_code',
}

token_response = requests.post(token_url, data=token_params)
access_token = token_response.json()['access_token']

# Initiate Telegram and reply to commands
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command('start') & filters.private)
def cmd1(client, message):
    client.send_message(message.chat.id, 'Hello, to check your Strava activities type /activities')

@app.on_message(filters.command('activities') & filters.private)
def cmd2(client, message):
    activities_url = f'{url}athlete/activities'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(activities_url, headers=headers)
    activities = response.json()

    activity_message = 'Your Strava activities:\n'
    for activity in activities:
        activity_message += f"{activity['name']} - {activity['distance']} meters\n"

    client.send_message(message.chat.id, activity_message)

app.run()
