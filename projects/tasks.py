from celery import shared_task
import requests
from celery import shared_task
from projects.models import City
from django.shortcuts import get_object_or_404
api_key = '4ad6e920-3cd1-4f0c-987e-e95550d1f998'


@shared_task(name='summary')
def request_to_source():
    Almaty = get_object_or_404(City, name='Almaty')
    Astana = get_object_or_404(City, name='Astana')
    print(Almaty, Astana)
    urls = [f'http://api.airvisual.com/v2/city?city=Nur-sultan&state=Nur-sultan&country=Kazakhstan&key={api_key}',
            f'http://api.airvisual.com/v2/city?city=Almaty&state=Almaty Qalasy&country=Kazakhstan&key={api_key}']
    for url in urls:
        k = requests.get(url).json()
        if k['data']['city'] == 'Nur-Sultan':
            Astana.aqi_us = k['data']['current']['pollution']['aqius']
            Astana.main_pollutant_us = k['data']['current']['pollution']['mainus']
        elif k['data']['city'] == 'Almaty':
            Almaty.aqi_us = k['data']['current']['pollution']['aqius']
            Almaty.main_pollutant_us = k['data']['current']['pollution']['mainus']
        # elif k['data']['city'] == 'Atyrau':
        #     Astana.aqi_us = k['data']['current']['pollution']['aqius']
        #     Astana.main_pollutant_us = k['data']['current']['pollution']['mainus']
        # elif k['data']['city'] == 'Pavlodar':
        #     Astana.aqi_us = k['data']['current']['pollution']['aqius']
        #     Astana.main_pollutant_us = k['data']['current']['pollution']['mainus']
