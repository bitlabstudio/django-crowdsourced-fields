"""Tests for the models of the ``django-crowdsourced-fields`` app."""
from django.test import TestCase

from crowdsourced_fields.tests.factories import CrowdsourcedItemFactory


class CrowdsourcedItemTestCase(TestCase):
    """Tests for the ``CrowdsourcedItem`` model."""
    def test_model(self):
        item = CrowdsourcedItemFactory()
        self.assertTrue(item.pk, msg=(
            'Should be able to create a new instance of this model'))
