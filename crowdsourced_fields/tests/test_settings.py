"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True

CURRENT_DIR = os.path.dirname(__file__)

DATABASES={
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF='crowdsourced_fields.tests.urls'

STATIC_URL='/static/'

STATIC_ROOT=os.path.join(CURRENT_DIR, '../../static/')

STATICFILES_DIRS=(
    os.path.join(CURRENT_DIR, 'test_static'),
    os.path.join(CURRENT_DIR, '../static'),
)

TEMPLATE_DIRS=(
    os.path.join(CURRENT_DIR,'../templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR=os.path.join(
    CURRENT_DIR, 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'test_app$', 'settings$', 'urls$', 'locale$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]

INTERNAL_APPS = [
    'django_nose',
    'crowdsourced_fields.tests.test_app',
    'crowdsourced_fields',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
