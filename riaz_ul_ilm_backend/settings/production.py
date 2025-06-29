from .base import *

DEBUG = False

# Read ALLOWED_HOSTS from environment variable and convert to a list
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Get CORS_ALLOWED_ORIGINS from .env and split into a list
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

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



# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')  # or your email provider's SMTP server
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Use your app-specific password here
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Live Redis URL (for production)
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")