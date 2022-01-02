import os
from googleapiclient.discovery import build

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    q='요리',
    type='videos',
).execute()

for item in search_response['items']:
    print(item['snippet']['title'])