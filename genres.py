import requests

API_KEY = "5b42a28ceb234a5da8d6d1105ae75894"
response = requests.get(f"https://api.rawg.io/api/genres?key={API_KEY}")
genres = response.json()
for genre in genres['results']:
    print(f"Name: {genre['name']}, Slug: {genre['slug']}")
