from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen
from django.conf import settings

from . import app_settings

if settings.DEBUG:
    html = open(app_settings.PWA_SERVICE_WORKER_PATH).read()
else:
    html = urlopen(app_settings.PWA_SERVICE_WORKER_PATH).read()

def service_worker(request):
    return HttpResponse(html, content_type='application/javascript')

def manifest(request):
    return render(request, 'manifest.json', {
        setting_name: getattr(app_settings, setting_name)
        for setting_name in dir(app_settings)
        if setting_name.startswith('PWA_')
    }, content_type='application/json')