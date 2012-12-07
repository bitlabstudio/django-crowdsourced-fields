"""Tests for the forms of the ``django-crowdsourced-fields`` app."""
from django.test import TestCase

from crowdsourced_fields.tests.models_tests import create_fixtures
from crowdsourced_fields.tests.test_app.forms import DummyModelForm


class CrowdsourcedFieldsFormMixinTestCase(TestCase):
    """Tests for the ``CrowdsourcedFieldsFormMixin`` mixin."""
    longMessage = True

    def test_mixin(self):
        create_fixtures(self)
        form = DummyModelForm()
        result = form.country_crowdsourced_values()
        self.assertEqual(result, '["Germany", "Singapore"]', msg=(
            'Should add ``fieldname_crowdsourced_values`` methods to the form'
            " and these methods should return all values for that fields's"
            " item type"))

    def test_initial_value(self):
        create_fixtures(self)
        self.dummy.country = 'GERMANY'
        self.dummy.save()
        form = DummyModelForm(instance=self.dummy)
        self.assertEqual(form.initial['country'], self.item.value)
