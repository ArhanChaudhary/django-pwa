""" Settings required by django-app. """
from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import get_script_prefix
from django.utils.functional import lazy
import os

# Lazy-evaluate URLs so including pwa.urls in root urlconf works
resolve_url = lazy(resolve_url, str)

# Get script prefix for apps not mounted under /
_PWA_SCRIPT_PREFIX = get_script_prefix()

# Path to the service worker implementation.  Default implementation is empty.
PWA_SERVICE_WORKER_PATH = getattr(settings, 'PWA_SERVICE_WORKER_PATH',
                                  os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates',
                                               'serviceworker.js'))
# App parameters to include in manifest.json and appropriate meta tags
PWA_APP_NAME = getattr(settings, 'PWA_APP_NAME', 'MyApp')
PWA_APP_DESCRIPTION = getattr(settings, 'PWA_APP_DESCRIPTION', 'My Progressive Web App')
PWA_APP_ROOT_URL = resolve_url(getattr(settings, 'PWA_APP_ROOT_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_THEME_COLOR = getattr(settings, 'PWA_APP_THEME_COLOR', '#000')
PWA_APP_BACKGROUND_COLOR = getattr(settings, 'PWA_APP_BACKGROUND_COLOR', '#fff')
PWA_APP_DISPLAY = getattr(settings, 'PWA_APP_DISPLAY', 'standalone')
PWA_APP_SCOPE = resolve_url(getattr(settings, 'PWA_APP_SCOPE', _PWA_SCRIPT_PREFIX))
PWA_APP_DEBUG_MODE = getattr(settings, 'PWA_APP_DEBUG_MODE', True)
PWA_APP_ORIENTATION = getattr(settings, 'PWA_APP_ORIENTATION', 'any')
PWA_APP_START_URL = resolve_url(getattr(settings, 'PWA_APP_START_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_FETCH_URL = resolve_url(getattr(settings, 'PWA_APP_FETCH_URL', _PWA_SCRIPT_PREFIX))
PWA_APP_STATUS_BAR_COLOR = getattr(settings, 'PWA_APP_STATUS_BAR_COLOR', 'default')
PWA_APP_ICONS = getattr(settings, 'PWA_APP_ICONS', [
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-72x72.png',
        'sizes': '72x72',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-96x96.png',
        'sizes': '96x96',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-128x128.png',
        'sizes': '128x128',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-144x144.png',
        'sizes': '144x144',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-152x152.png',
        'sizes': '152x152',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-192x192.png',
        'sizes': '192x192',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-384x384.png',
        'sizes': '384x384',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/icon-512x512.png',
        'sizes': '512x512',
        "type": "image/png",
        'purpose': 'any',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-72x72.png',
        'sizes': '72x72',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-96x96.png',
        'sizes': '96x96',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-128x128.png',
        'sizes': '128x128',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-144x144.png',
        'sizes': '144x144',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-152x152.png',
        'sizes': '152x152',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-192x192.png',
        'sizes': '192x192',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-384x384.png',
        'sizes': '384x384',
        "type": "image/png",
        'purpose': 'maskable',
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/maskable-icon-512x512.png',
        'sizes': '512x512',
        "type": "image/png",
        'purpose': 'maskable',
    }
])
PWA_APP_SPLASH_SCREEN = getattr(settings, 'PWA_APP_SPLASH_SCREEN', [
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "640x1136"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-750x1334.png',
        'media': '(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "750x1334"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1242x2208.png',
        'media': '(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)',
        "sizes": "1242x2208"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1125x2436.png',
        'media': '(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)',
        "sizes": "1125x2436"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-828x1792.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "828x1792"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1242x2688.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)',
        "sizes": "1242x2688"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1536x2048.png',
        'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "1536x2048"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1668x2224.png',
        'media': '(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "1668x2224"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-1668x2388.png',
        'media': '(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "1668x2388"
    },
    {
        'src': 'https://storage.googleapis.com/twstatic/images/icons/splash-2048x2732.png',
        'media': '(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)',
        "sizes": "2048x2732"
    }

])
PWA_APP_DIR = getattr(settings, 'PWA_APP_DIR', 'auto')
PWA_APP_LANG = getattr(settings, 'PWA_APP_LANG', 'en-US')
