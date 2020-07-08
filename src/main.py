#!/usr/bin/env python3
import requests
import json

query = requests.get('https://api.exchangeratesapi.io/latest?base=USD')

q = query.text


media = json.loads(q)

media2 = (media.get('rates'))
print(media2.get('PLN'))