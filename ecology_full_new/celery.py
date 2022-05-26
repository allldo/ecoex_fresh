from __future__ import absolute_import
import os
from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task
# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
from ecology_full_new import settings
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecology_full_new.settings')

# you change change the name here
app = Celery("django_celery_example")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# from landing.models import

api_key = '4ad6e920-3cd1-4f0c-987e-e95550d1f998'


# crontab нормальный сделать
@periodic_task(run_every=(crontab(minute='*/60')), name="request_to_source", ignore_result=True)
def request_to_source():
    url = f'http://api.airvisual.com/v2/city?city=Nur-sultan&state=Nur-sultan&country=Kazakhstan&key={api_key}'
    urls = [f'http://api.airvisual.com/v2/city?city=Nur-sultan&state=Nur-sultan&country=Kazakhstan&key={api_key}', f'http://api.airvisual.com/v2/city?city=Almaty&state=Almaty Qalasy&country=Kazakhstan&key={api_key}']
    for url in urls:
        requests.get(url)