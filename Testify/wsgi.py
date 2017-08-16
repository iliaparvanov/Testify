"""
WSGI config for Testify project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

# add your project directory to the sys.path
project_home = u'/home/Testify'
if project_home not in sys.path:
    sys.path.append(project_home)


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Testify.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
