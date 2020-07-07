import requests
import json

query = requests.get('https://api.exchangeratesapi.io/latest?base=USD')

q = query.text


media = json.loads(q)
print(media)