"""Tests for the models of the ``django-crowdsourced-fields`` app."""
from django.test import TestCase

from crowdsourced_fields.models import CrowdsourcedItemGenericForeignKey
from crowdsourced_fields.tests.factories import CrowdsourcedItemFactory
from crowdsourced_fields.tests.test_app.models import DummyModel


def create_fixtures(cls):
    """
    Creates fixtures that we need for many tests.

    Creates a dummy object and a crowdsourced item and connects both with a
    ``CrowdsourcedFieldsModelMixinTestCase``.

    """
    cls.dummy = DummyModel.objects.create(
        title='Dr', name='Foobar', country='Germany')
    cls.item = CrowdsourcedItemFactory()
    cls.fk = CrowdsourcedItemGenericForeignKey.objects.create(
        content_object=cls.dummy, item=cls.item, item_type=cls.item.item_type)


class CrowdsourcedFieldsModelMixinTestCase(TestCase):
    """Tests for the ``CrowdsourcedFieldsModelMixin`` mixin."""
    def test_mixin(self):
        dummy = DummyModel()
        self.assertTrue(hasattr(dummy, 'country_crowdsourced'), msg=(
            'Should add the method `country_crowdsourced` to the model'))
        self.assertTrue(hasattr(dummy, 'title_crowdsourced'), msg=(
            'Should add the method `title_crowdsourced` to the model'))

    def test_dynamically_added_method(self):
        create_fixtures(self)
        result = self.dummy.country_crowdsourced()
        self.assertEqual(result, self.item.value)


class CrowdsourcedItemTestCase(TestCase):
    """Tests for the ``CrowdsourcedItem`` model."""
    def test_model(self):
        item = CrowdsourcedItemFactory()
        self.assertTrue(item.pk, msg=(
            'Should be able to create a new instance of this model'))


class CrowdsourcedItemGenericForeignKeyTestCase(TestCase):
    """Tests for the ``CrowdsourcedItemGenericForeignKey`` model."""
    def test_model(self):
        create_fixtures(self)
        self.assertTrue(self.fk.pk, msg=('Should be able to save the model'))
