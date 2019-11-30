import requests
import json
API_KEY = 'cKEMX2RxaRH65WT2Tq7QB2a0zGBXN8R8'
url = 'https://api.giphy.com/v1/gifs/random'
key = 'yes'
res = requests.get(f'{url}?api_key={API_KEY}&tag={key}&rating=g')
print(json.dumps(res.json(), indent=2))

print(res.json()['data']['images']['fixed_height_small_still']['url'])