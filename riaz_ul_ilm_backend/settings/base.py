import os
from dotenv import load_dotenv
from pathlib import Path
# from celery.schedules import crontab
from datetime import timedelta

load_dotenv()

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
    # 'django_celery_beat',

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Media Settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# # Celery settings
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'


# # Celery Beat (task scheduler) settings
# CELERY_BEAT_SCHEDULE = {
#     'clean_local_video_assets': {
#         'task': 'text2video.tasks.clean_local_video_assets',
#         'schedule': crontab(minute=0, hour='*/6'),  # Every 6 hours
#     },
#     'clean_supabase_storage': {
#         'task': 'text2video.tasks.clean_supabase_storage',
#         'schedule': crontab(minute='*/30', hour='*'),  # Every 30 minutes
#     },
#     'mark_stuck_generations_as_failed': {
#         'task': 'text2video.tasks.mark_stuck_generations_as_failed',
#         'schedule': crontab(minute='*/15', hour='*'),  # Every 30 minutes
#     },
# }


# Supabse storage settings
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET_NAME = os.getenv("SUPABASE_BUCKET_NAME", "books")
SUPABASE_FOLDER_NAME = os.getenv("SUPABASE_FOLDER_NAME", "all_books")


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
    
    'EMAIL_FRONTEND_PROTOCOL' : 'http',  # Protocol for email links
    'EMAIL_FRONTEND_SITE_NAME' : "Riazulilm",
    'EMAIL_FRONTEND_DOMAIN': 'localhost:5173',  # Domain for email links

    # user serializer settings
    'SERIALIZERS': {
        'current_user': 'authapp.serializers.UserSerializer',  # path to your serializer
    },
}


# Custom User Model
AUTH_USER_MODEL = 'authapp.CustomUser'  # Use the custom user model


# # Cache settings
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",  # Correct backend
#         "LOCATION": "redis://localhost:6379/1",  # Redis database 1
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",  # Default client class
#         },
#     }
# }




# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1)
#     }