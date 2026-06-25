import requests
import json

artist = input("Enter the name of the artist ")

response = requests.get("https://itunes.apple.com/search?entity=song&term="+artist)

tracks_1 = response.json()
print(tracks_1)
print(f"Songs of artist {artist}")
for result in tracks_1["results"]:
    track_name = result["trackName"]
    download_preview = result["previewUrl"]
    print(f"Song name: {track_name}\nDownload song preview: {download_preview}")

