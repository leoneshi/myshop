import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('django.conf:settings','myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf：settings')
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
