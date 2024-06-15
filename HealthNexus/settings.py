import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'healthnexus.bwenge.com']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'social_django',
    'widget_tweaks',
]

# Database Configuration example (using PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.env('EMAIL_HOST_PASSWORD')

# Social Authentication (Google OAuth2)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.env('GOOGLE_OAUTH_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.env('GOOGLE_OAUTH_CLIENT_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://yourdomain.com/accounts/google/login/callback/'

# Other settings...
# AUTH_USER_MODEL, LOGOUT_REDIRECT_URL, LOGIN_URL, etc.

# Jazzmin Settings
JAZZMIN_SETTINGS = {
    "site_title": "HealthNexus ADMIN",
    "site_header": "HealthNexus",
    "site_brand": "HealthNexus",
    "login_logo": None,
    "copyright": "HealthNexus",
}

# Additional settings as needed...
