"""
WSGI config for riaz_ul_ilm_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables
load_dotenv()

# Get the environment (defaults to 'local' if not set)
ENVIRONMENT = os.getenv('DJANGO_ENV', 'local')

# Set the correct settings module based on the environment
if ENVIRONMENT == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riaz_ul_ilm_backend.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'riaz_ul_ilm_backend.settings.local')

application = get_wsgi_application()
