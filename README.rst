Django Crowdsourced Fields
==========================

**WORK IN PROGRESS. DO NOT USE THIS!**

A reusable Django app that allows to mark certain fields of your models as
masterdata. Users would still be able to enter their own values but the app
will map them to unique instances. Admin staff is able to review all user
generated entriesand mark them as approved.

An example could be a vehicle site, where you would like to allow users to
enter make and model for their vehicle but you want to make sure that an
entry of "bmw" and "Bmw" results in "BMW".

The app also comes with a nice jQuery combobox for such fields, where user get
autosuggestions while they type.

Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django
    pip install South

If you want to install the latest stable release from PyPi::

    $ pip install django-crowdsourced-fields

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-crowdsourced-fields.git#egg=crowdsourced_fields

Add ``crowdsourced_fields`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'crowdsourced_fields',
    )

Don't forget to migrate your database::

    ./manage.py migrate crowdsourced_fields

Add jQuery and jQuery UI to your base template or at least to the template that 
should display forms with crowdsourced fields. Also include the jquery UI
styles and special styles provided by this app::

    <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/flick/jquery-ui.css">
    {{ form.media.css }}

    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js" type="text/javascript" charset="utf-8"></script>
    {{ form.media.js }}

You might want to include the jquery and jquery UI parts in your base template
and the ``{{ form.media }}`` parts only in the template that uses a form with
crowdsourced fields.

Usage
-----

Prepare your models
+++++++++++++++++++

First you need to modify the model that should have crowdsourced fields::

    from crowdsourced_fields.models import CrowdSourcedModelMixin

    class YourModel(CrowdsourcedModelMixin, models.Model):
        CROWDSOURCED_FIELDS = {
            'make': {'item_type': 'makes', }
            'model': {'item_type': 'models', }
        }

        make = models.CharField(...)
        model = models.CharField(...)

``CROWDSOURCED_FIELDS`` is a dictionary of dictionaries. The main keys are the
fields that should be crowdsourced. This must be ``CharFields``.

The inner dictionary supports the following keys as settings:

2. **item_type (mandatory)**: The name of the group under which the data of
   this field should be grouped. Let's assume you have two models and both have
   a field ``country`` which should have access to the same data. By giving
   the same ``item_type`` for the field on both models, they will use the same
   set of crowdsourced data.

For each field that you selected, the mixin will dynamically add a method
called ``fieldname_crowdsourced`` to the model. Therefore we will save both,
the value that the user actually entered (in it's original field) and a link to 
the unique and approved value that we maintain through this app.

For your staff users it is save to change the values of the
``CrowdsourcedItem`` objects. Since you should use those in your templates,
any typo fixes would be reflected on your site immediately without the need
of a datamigration.

Create a model form
+++++++++++++++++++

Next you would create a ``ModelForm`` for your model with crowdsourced fields::

    from django import forms
    from crowdsourced_fields.forms import CrowdsourcedFieldsFormMixin
    from your_app.models import YourModel

    class YourModelForm(CrowdsourcedFieldsFormMixin, forms.ModelForm):
        class Meta:
            model = YourModel

The ``CrowdsourcedFieldsFormMixin`` will do the magic for you and add replace
the original form field (a text input) with a combobox that has all existing
values ready for autosuggest.

Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-crowdsourced-fields
    $ pip install -r requirements.txt
    $ ./online_docs/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ ./crowdsourced_fields/tests/runtests.sh
    # You should still get no failing tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.

If you are making changes that need to be tested in a browser (i.e. to the
CSS or JS files), you might want to setup a Django project, follow the
installation insttructions above, then run ``python setup.py develop``. This
will just place an egg-link to your cloned fork in your project's virtualenv.

Roadmap
-------

Check the issue tracker on github for milestones and features to come.
