// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    'https://storage.googleapis.com/twstatic/misc/icons/icon_72x72.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_96x96.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_128x128.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_144x144.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_152x152.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_192x192.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_384x384.png',
    'https://storage.googleapis.com/twstatic/misc/icons/icon_512x512.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_640x1136.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_750x1334.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1242x2208.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1125x2436.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_828x1792.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1242x2688.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1536x2048.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1668x2224.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_1668x2388.png',
    'https://storage.googleapis.com/twstatic/misc/icons/splash_2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                
            })
    )
});
