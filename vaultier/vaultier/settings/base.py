import os.path
import sys
from celery.schedules import crontab

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    '..'
)

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vaultier',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}
if 'test' in sys.argv or 'test_coverage' in sys.argv:  # Covers regular testing and django-coverage
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ('vaultier', os.path.join(PROJECT_PATH, 'scripts', 'dist')),
)

SITE_URL = 'http://localhost:8000/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4*1g_d$&2ur&i0$bp^yh!16@$6nq#e^5_=isv9h2!ud8+3%grm'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'vaultier.business.middleware.DisableCSRFMiddleware.DisableCSRFMiddleware'
)

ROOT_URLCONF = 'vaultier.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'vaultier.wsgi.application'

# Template settings
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'vaultier/tempates'),
    os.path.join(BASE_DIR, 'vaultier/business'),
    os.path.join(PROJECT_PATH, 'vaultier'),

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',

    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'accounts.business.authentication.TokenAuthentication',
    ),
}

COMPRESS_ENABLED = 1

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'south',
    'rest_framework',
    'accounts',
    'acls',
    'cards',
    'search',
    'secrets',
    'vaults',
    'versions',
    'workspaces',
    'slugs',
    'kombu.transport.django'

)

# Sentry site_id
SITE_ID = 1

# SCM dealer to provide git revision
DEALER_TYPE = 'git'

# SCM dealer path to git
DEALER_PATH = './../'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)-15s %(name)-7s %(levelname)s: %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('accounts.business.authentication.Backend', )

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

EMBER_TPL_DIR = os.path.join(PROJECT_PATH, 'static/js/module')
EMBER_TPL_CMPDIR = os.path.join(PROJECT_PATH, 'static/tpl')
EMBER_TPL_MASK = "\w+.hbs$"

# Indicates options for frontend
FT_FEATURES = {
    'dev_shared_key': False,  # True to use/generate same key for all users
    # sentry key to be used for loggin errors on the frontend
    'raven_key': 'http://df6466226ad14775b23818b42df3a5c8@sentry.rclick.cz/5'
}

# Indicates options for backed
BK_FEATURES = {
    'dev_mail_to': False,  # 'email@example.com' to send all emails to this address
    'dev_shared_key': False,  # True to use/generate same key for all users
    # 1 hour in milliseconds used to calculate the expiration time on api.lostkey module
    'lostkey_hash_expiration_time': 3600000,
    'from_email': 'info@rclick.com',  # Default email address from which we send emails
    'ga_create_code': 'UA-17830772-11',  # code for google analytics
    'login_safe_timestamp_delta': 15,  # Max difference between timestamp from server and from front-end in seconds
}

VAULTIER = {
    # token lifetime (in hours)
    'authentication_token_lifetime': 2,
    # last_used_at will be renewed after some interval (in minutes)
    'authentication_token_renewal_interval': 1,
    'invitation_lifetime': 7,
    # When anonymous usage statistics is enabled, vaultier periodically
    # anonymously notifies its maintainer and developer about running
    # instance of Valtier.
    # As Vaultier is Open Source we kindly ask you to leave this option
    # enabled and let us know how many instances are deployed.
    # We send these statistics data: count of workspaces, vaults,cards,
    # secrets, users, members
    'allow_anonymous_usage_statistics': True
}

#celery broker
BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERYBEAT_SCHEDULE = {
    'garbage_collector_tokens': {
        'task': 'accounts.tasks.task_token_garbage_collector',
        'schedule': crontab(hour='*/6'),
    },
    'usage_statistics': {
        'task': 'vaultier.tasks.task_statistics_collector',
        # every day in 1 am
        'schedule': crontab(hour='1'),
    }
}