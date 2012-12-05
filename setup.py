import os
from setuptools import setup, find_packages
import crowdsourced_fields


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-crowdsourced-fields",
    version=crowdsourced_fields.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, ORM, jQuery, combobox, models, fields',
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/bitmazk/django-crowdsourced-fields",
    packages=find_packages(),
    include_package_data=True,
    tests_require=[
        'fabric',
        'factory_boy',
        'django-nose',
        'coverage',
        'django-coverage',
        'selenium',
    ],
    test_suite='crowdsourced_fields.tests.runtests.runtests',
)
