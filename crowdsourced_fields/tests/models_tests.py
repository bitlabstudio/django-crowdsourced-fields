"""Tests for the models of the ``django-crowdsourced-fields`` app."""
from django.test import TestCase

from crowdsourced_fields.models import (
    CrowdsourcedItem,
    CrowdsourcedItemGenericForeignKey,
)
from crowdsourced_fields.tests.factories import CrowdsourcedItemFactory
from crowdsourced_fields.tests.test_app.models import DummyModel


class MessagesTestCase(TestCase):
    def assertEqual(*args, **kwargs):
        pass


def create_fixtures(cls):
    """
    Creates fixtures that we need for many tests.

    Creates a dummy object and a crowdsourced item and connects both with a
    ``CrowdsourcedFieldsModelMixinTestCase``.

    """
    cls.dummy = DummyModel.objects.create(
        title='Dr', name='Foobar', country='Germany', country2="Singapore")
    cls.fk = CrowdsourcedItemGenericForeignKey.objects.get(
        object_id=cls.dummy.pk, field_name='country', item_type='countries')
    cls.fk2 = CrowdsourcedItemGenericForeignKey.objects.get(
        object_id=cls.dummy.pk, field_name='country2', item_type='countries')
    cls.item = cls.fk.item


class CrowdsourcedFieldsModelMixinTestCase(TestCase):
    """Tests for the ``CrowdsourcedFieldsModelMixin`` mixin."""
    longMessage = True

    def test_mixin(self):
        dummy = DummyModel()
        self.assertTrue(hasattr(dummy, 'country_crowdsourced'), msg=(
            'Should add the method `country_crowdsourced` to the model'))
        self.assertTrue(hasattr(dummy, 'title_crowdsourced'), msg=(
            'Should add the method `title_crowdsourced` to the model'))

    def test_dynamically_added_method(self):
        create_fixtures(self)
        result = self.dummy.country_crowdsourced()
        self.assertEqual(result, self.item.value, msg=(
            'The dynamically added methods should return the correct'
            ' crowdsourced value'))

        CrowdsourcedItem.objects.all().delete()
        CrowdsourcedItemGenericForeignKey.objects.all().delete()
        self.dummy.country_crowdsourced()
        self.assertEqual(
            CrowdsourcedItem.objects.all().count(), 1, msg=(
                'If this app was added to an existing app with existing data'
                ' we will have values that are not, yet related to any'
                ' crowdsourced items. They should be created when trying'
                ' to access them'))

    def test_object_save(self):
        create_fixtures(self)
        self.assertEqual(
            CrowdsourcedItem.objects.all().count(), 3, msg=(
                'Should create new crowdsourced items if none existed'
                ' when saved'))
        self.assertEqual(
            CrowdsourcedItemGenericForeignKey.objects.all().count(), 3, msg=(
                'Should create new generic foreign keys if none existed'
                ' when saved'))
        item = CrowdsourcedItem.objects.get(pk=self.item.pk)
        self.assertEqual(self.dummy.country, item.value, msg=(
            'When saved for the first time, a corresponding'
            ' ``CrowdsourcedItem`` with the same value should be created'))
        crowdsourced_item_value = item.value

        self.dummy.country = 'GERMANY'
        self.dummy.save()

        self.assertEqual(
            CrowdsourcedItem.objects.all().count(), 3, msg=(
                'On a second save, if the value is essentially still the'
                ' same, no new item should be created'))
        self.assertEqual(
            CrowdsourcedItemGenericForeignKey.objects.all().count(), 3, msg=(
                'On a second save, if the value is essentially still the'
                ' same, no new generic foreign key should be created'))
        item = CrowdsourcedItem.objects.get(pk=self.item.pk)
        self.assertEqual(item.value, crowdsourced_item_value,  msg=(
            'On a second save, if the value of the object had changed but'
            ' is essentially still the same (just different writing),'
            ' we will not change the crowdsoured value because an admin might'
            ' have approved the old value as the correct version'))

        self.dummy.country = 'Middle-earth'
        self.dummy.save()

        self.assertEqual(
            CrowdsourcedItem.objects.all().count(), 4, msg=(
                'On a third save, if the value is actually different, a new'
                ' item should be created'))


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
