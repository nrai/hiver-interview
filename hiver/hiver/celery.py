import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hiver.conf.local')

app = Celery('hiver')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
