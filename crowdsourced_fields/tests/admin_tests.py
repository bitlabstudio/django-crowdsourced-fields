"""Tests for admin classes of the ``django-crowdsourced-fields`` app."""
from django.test import TestCase

from crowdsourced_fields.admin import approve_items
from crowdsourced_fields.models import CrowdsourcedItem
from crowdsourced_fields.tests.models_tests import create_fixtures


class ApproveItemsTestCase(TestCase):
    """Tests for the ``approve_items`` admin action."""
    def test_action(self):
        create_fixtures(self)
        user_generated_items = CrowdsourcedItem.objects.filter(
            is_user_generated=True)
        self.assertEqual(user_generated_items.count(), 2, msg=(
            'We assume that our fixtures have two user generated items'))
        queryset = CrowdsourcedItem.objects.filter(pk__in=[
            user_generated_items[0].pk, user_generated_items[1].pk])

        approve_items(None, None, queryset)
        user_generated_items = CrowdsourcedItem.objects.filter(
            is_user_generated=True)
        self.assertEqual(user_generated_items.count(), 0, msg=(
            'Should set `is_user_generated` to `False` for all selected'
            ' items'))
