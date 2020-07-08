#!/usr/bin/env python3
import requests
import json

base_currency = input('Start -> ')
final_currency = input('Final -> ')
units_of_currency = float(input('How much? -> '))


def func(base, final, units):
    query = requests.get('https://api.exchangeratesapi.io/latest?base=' + base.upper())

    q = query.text

    media = json.loads(q)

    media2 = (media.get('rates'))
    print(float(media2.get(final.upper()) * units))


func(base_currency, final_currency, units_of_currency)
