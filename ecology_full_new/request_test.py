import os

import requests, json
api_key = '4ad6e920-3cd1-4f0c-987e-e95550d1f998'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'info.json'))
json_data = json.load(file)
urls = [f'http://api.airvisual.com/v2/city?city=Nur-sultan&state=Nur-sultan&country=Kazakhstan&key={api_key}',
        f'http://api.airvisual.com/v2/city?city=Almaty&state=Almaty Qalasy&country=Kazakhstan&key={api_key}']
json_data = json_data['data']['current']['pollution']
# print(json_data.values())
# for parameter in json_data:
    # print(parameter, ' - ', json_data.get(parameter))

file.close()


for url in urls:
    json_datka = requests.get(url).json()['data']['current']['pollution']
    for parameter in json_datka:
        print(parameter, ' - ', json_datka.get(parameter))