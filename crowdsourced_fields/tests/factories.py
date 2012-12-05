"""Factories for the models of the ``django-crowdsourced-fields`` app."""
import factory

from crowdsourced_fields.models import CrowdsourcedItem


class CrowdsourcedItemFactory(factory.Factory):
    """Factory for the ``CrowdsourcedItem`` model."""
    FACTORY_FOR = CrowdsourcedItem

    item_type = 'countries'
    value = 'Germany'
