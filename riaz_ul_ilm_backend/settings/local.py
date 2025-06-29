from .base import *
import os

DEBUG = True

# Read ALLOWED_HOSTS from environment variable and convert to a list
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Get CORS_ALLOWED_ORIGINS from .env and split into a list
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'http://localhost:5173', 'http://localhost:4173']


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('SUPABASE_DB_NAME'),      # Supabase database name
        'USER': os.getenv('SUPABASE_DB_USER'),      # Supabase username (usually 'postgres')
        'PASSWORD': os.getenv('SUPABASE_DB_PASSWORD'),  # Your Supabase database password
        'HOST': os.getenv('SUPABASE_DB_HOST'),      # Supabase session pooler host (host URL, without 'postgresql://')
        'PORT': os.getenv('SUPABASE_DB_PORT', '5432'),  # Default PostgreSQL port
    }
}

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# Local Redis URL for local testing
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"