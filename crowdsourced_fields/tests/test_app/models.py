"""Dummy model needed for tests."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DummyModel(models.Model):
    """Dummy model needed for testing purposes."""
    CROWDSOURCED_FIELDS = ['country', 'title', ]

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
