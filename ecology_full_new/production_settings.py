from celery.schedules import crontab

from ecology_full_new.celery import app

CELERY_BROKER_URL = 'redis://localhost:6379'
# If time zones are active (USE_TZ = True) define your local CELERY_TIMEZONE = 'Asia/Kolkata'
app.conf.enable_utc = False # so celery doesn't take utc by default
# We're going to have our tasks rolling soon, so that will be handy CELERY_BEAT_SCHEDULE = {}

CELERY_TIMEZONE = 'Asia/Almaty'
# Let's make things happen
CELERY_BEAT_SCHEDULE = {
 'send-summary-every-hour': {
       'task': 'summary',
       'schedule': 3600.0,
    },
}