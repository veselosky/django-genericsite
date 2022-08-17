"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
VAR = BASE_DIR / "var"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ri51as9!afs^d0y_&%cf#jv)uud!dfky0k0ydioc_3u^va&5^+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ALLOWED_HOSTS = []
SITE_ID = 1
LOGIN_REDIRECT_URL = "/"


# Application definition

INSTALLED_APPS = [
    "genericsite",
    # 3rd party apps for "full" usage style
    "django_bootstrap_icons",
    "easy_thumbnails",  # via filer
    "filer",
    "mptt",  # via filer
    "django_extensions",
    "taggit",
    "tinymce",
    # Standard Django stuff
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # UpdateCacheMiddleware must be above LocaleMiddleware
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "test_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "test_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": VAR / "db.sqlite3",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "static/"
STATIC_ROOT = VAR / "static"
MEDIA_ROOT = VAR / "media"
MEDIA_URL = "media/"
if not STATIC_ROOT.exists():
    STATIC_ROOT.mkdir(parents=True, exist_ok=True)
if not MEDIA_ROOT.exists():
    MEDIA_ROOT.mkdir(parents=True, exist_ok=True)

FILER_DEBUG = FILER_ENABLE_LOGGING = DEBUG
FILER_IMAGE_MODEL = "genericsite.ImageFile"
FILER_FILE_MODELS = (
    FILER_IMAGE_MODEL,
    "genericsite.VideoFile",
    "genericsite.AudioFile",
    "filer.File",
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    #'easy_thumbnails.processors.scale_and_crop',
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
