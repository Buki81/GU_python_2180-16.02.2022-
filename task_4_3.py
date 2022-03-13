import requests
from decimal import Decimal
import datetime


def currency_rates(code):
    content = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if code.upper() in content:
        curr = content.split(code.upper())[1].split('<Value>')[1].split('</')[0]
        currency = Decimal(curr.replace(',', '.')).quantize(Decimal("1.00"))
        date = datetime.datetime.strptime(content.split('Date="')[1].split('"')[0], '%d.%m.%Y').strftime('%d.%m.%Y')
        print(currency, date)
    else:
        print('None')

currency_rates('usd')
currency_rates('USD')
currency_rates('eur')
currency_rates('EUR')