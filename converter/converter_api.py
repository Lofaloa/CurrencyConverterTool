import requests
from datetime import date
import xml.etree.ElementTree as ET

def get_conversion_amount(form):
    URL = "http://currencyconverter.kowabunga.net/converter.asmx/GetConversionRate?"
    args= {
        "CurrencyFrom": form.cleaned_data['currency_from'],
        "CurrencyTo": form.cleaned_data['currency_to'],
        "RateDate": date.today(),
        "Amount": form.cleaned_data['amount']
    }
    return requests.get(url=URL, params=args).content

def get_currencies():
    URL = "http://currencyconverter.kowabunga.net/converter.asmx/GetCurrencies?"
    return requests.get(url=URL)

def get_currencies_tuple():
    root = ET.fromstring(get_currencies().text)
    currencies = []
    index = 0
    for child in root:
        element = (index, child.text)
        index += 1
        currencies.append(element)
    return tuple(currencies)
