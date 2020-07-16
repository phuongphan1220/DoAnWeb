"""
WSGI config for DoAnWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
import sys

path = '/home/doanwebcnpm/DoAnWeb'
if path not in sys.path:
 sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'DoAnWeb.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())