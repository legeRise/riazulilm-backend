import os
from dotenv import load_dotenv
from pathlib import Path
# from celery.schedules import crontab
from datetime import timedelta

load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authapp',
    'books',
    'rest_framework',
    'corsheaders',
    'djoser',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'riaz_ul_ilm_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'riaz_ul_ilm_backend.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# R2 Storage settings
R2_ENDPOINT_URL= os.getenv("R2_ENDPOINT_URL", "") 
R2_ACCESS_KEY_ID= os.getenv("R2_ACCESS_KEY_ID", "")  
R2_SECRET_ACCESS_KEY= os.getenv("R2_SECRET_ACCESS_KEY", "")  
R2_BUCKET_NAME= os.getenv("R2_BUCKET_NAME", "riazulilm-books")  



CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name": 'riazulilm-static', # special bucket for static files 
    "default_acl": "public-read",  # "private"
    "signature_version": "s3v4",
    "endpoint_url": R2_ENDPOINT_URL,
    "access_key": R2_ACCESS_KEY_ID,
    "secret_key": R2_SECRET_ACCESS_KEY, 
    "default_acl": "public-read",  # Set to "private" if you want private access
    "region_name": "auto",  # Use "auto" for Cloudflare R2
    "signature_version": "s3v4",  # Use S3v4 signature version
    
    }


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            # this syntax means that this 'OPTIONS' dict will have all keys from the other dict + the location key as well
                    **CLOUDFLARE_R2_CONFIG_OPTIONS,
            "location": "media",  # key "default" refers to media files so this applies on ImageField and FileField
        },
    },
    # just like 'default' 'staticfiles' is a special key that refers to static files
    # else the ERRORS: (staticfiles.E005) The STORAGES setting must define a 'staticfiles' storage.
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            **CLOUDFLARE_R2_CONFIG_OPTIONS,
            "location": "static",  # Optional: specify a subdirectory for static files
        },
    },
}


# Authentication settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


# Djoser settings
DJOSER = {
    # signup settings
    'USER_CREATE_PASSWORD_RETYPE': True,  # signing up requires confirm_password(retype)
    
    # activate user settings
    'SEND_ACTIVATION_EMAIL': True,  #  sets 'is_active' to False by default, requires 'ACTIVATION_URL' to be set in DJOSER settings
    'ACTIVATION_URL': '#/activate/{uid}/{token}/',  # URL for activation
    
    
    # password reset settings
    'PASSWORD_RESET_CONFIRM_URL' : '#/password-reset/{uid}/{token}/', # Required to send reset password email
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND' : True,  # Show email not found message
    'PASSWORD_RESET_CONFIRM_RETYPE' : True,  # Confirm password retype
    
    'EMAIL_FRONTEND_PROTOCOL' : 'https',  # Protocol for email links
    'EMAIL_FRONTEND_SITE_NAME' : "Riazulilm",
    'EMAIL_FRONTEND_DOMAIN': 'riazulilm-frontend.onrender.com',  # Domain for email links

    # user serializer settings
    'SERIALIZERS': {
        'current_user': 'authapp.serializers.UserSerializer',  # path to your serializer
    },
}


# Custom User Model
AUTH_USER_MODEL = 'authapp.CustomUser'  # Use the custom user model


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1)
    }