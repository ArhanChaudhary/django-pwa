from django.test import TestCase
from django.template import Context, Template


class CreateMetaTemplateTagTest(TestCase):
    def setUp(self):
        context = Context({})
        template_to_render = Template(
            '{% load pwa %}'
            '{% progressive_web_app_meta %}'
        )
        self.rendered_template = template_to_render.render(context)

    def test_has_tags(self):
        """Must contains the tags in HTML"""
        tags = [
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_72x72.webp" sizes="72x72">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_96x96.webp" sizes="96x96">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_128x128.webp" sizes="128x128">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_144x144.webp" sizes="144x144">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_152x152.webp" sizes="152x152">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_192x192.webp" sizes="192x192">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_384x384.webp" sizes="384x384">',
            '<link rel="apple-touch-icon" href="https://storage.googleapis.com/twstatic/misc/icons/icon_512x512.webp" sizes="512x512">',
            '<link rel="manifest" href="/manifest.json">',
            '<meta name="mobile-web-app-capable" content="yes">',
            '<meta name="theme-color" content="#000">',
            '<meta name="apple-mobile-web-app-capable" content="yes">',
            '<meta name="apple-mobile-web-app-title" content="MyApp">',
            '<meta name="application-name" content="MyApp">',
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">',
            '<link rel="icon" sizes="512x512" href="https://storage.googleapis.com/twstatic/misc/icons/icon_512x512.webp">',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_640x1136.webp" media="(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_750x1334.webp" media="(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1242x2208.webp" media="(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1125x2436.webp" media="(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_828x1792.webp" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1242x2688.webp" media="(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1536x2048.webp" media="(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1668x2224.webp" media="(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_1668x2388.webp" media="(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<link href="https://storage.googleapis.com/twstatic/misc/icons/splash_2048x2732.webp" media="(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)" rel="apple-touch-startup-image"/>',
            '<meta name="msapplication-TileColor" content="#fff">',
            '<meta name="msapplication-TileImage" content="https://storage.googleapis.com/twstatic/misc/icons/icon_512x512.webp">'
        ]
        for text in tags:
            with self.subTest():
                self.assertInHTML(text, self.rendered_template)

    def test_has_serviceworker(self):
        """Must have the script tag with serviceworker registration"""
        contents = [
            '<script type="text/javascript">',
            "if ('serviceWorker' in navigator) {",
            "navigator.serviceWorker.register('/serviceworker.js', {",
            "scope: '/'",
            "}).then(function (registration) {",
            "console.log('django-pwa: ServiceWorker registration successful with scope: ', registration.scope);",
            "}, function (err) {",
            "console.log('django-pwa: ServiceWorker registration failed: ', err);",
            "});",
            "</script>"
        ]

        for expected in contents:
            with self.subTest():
                self.assertIn(expected, self.rendered_template)
