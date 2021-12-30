from django.conf.urls import url
from django.views.generic import RedirectView

from .views import manifest
from . import app_settings

# Serve up serviceworker.js and manifest.json at the root
urlpatterns = [
    url(r'^serviceworker\.js$', RedirectView.as_view(url=app_settings.PWA_SERVICE_WORKER_PATH), name='serviceworker'),
    url(r'^manifest\.json$', manifest, name='manifest')
]
