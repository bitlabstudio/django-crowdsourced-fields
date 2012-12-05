"""Dummy model needed for tests."""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from crowdsourced_fields.models import CrowdsourcedFieldsModelMixin


class DummyModel(CrowdsourcedFieldsModelMixin, models.Model):
    """Dummy model needed for testing purposes."""
    CROWDSOURCED_FIELDS = {
        'country': {'item_type': 'countries', },
        'title': {'item_type': 'titles', },
    }

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
    )

    name = models.CharField(
        max_length=256,
        verbose_name=_('Name'),
    )

    country = models.CharField(
        max_length=256,
        verbose_name=_('Country'),
    )
