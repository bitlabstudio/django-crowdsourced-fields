"""Models of the ``django-crowdsourced-fields`` app."""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CrowdsourcedItem(models.Model):
    """
    Something that is both, masterdata and user entered data.

    For example a `country` field: Maybe you don't know which countries exist
    in the world so you want to allow users to enter anything. But you want
    to approve all entries and make sure that the spelling and capitalization
    is correct.

    :item_type: You might have a ``country`` field on several of your models and
      you want the same autosuggestions for all models. Therefore you need to
      define an ``item_type`` in your ``CROWDSOURCED_FIELDS`` attribute. By
      giving the same ``item_type`` to your models it means that the collected
      data is available to all these models.

    :value: The value that the user has entered.

    :is_user_generated: If ``True`` it means that this item has been created
      based on user input (and not by an admin). Admins should regularly check
      all user generated items for spelling errors and set this to ``False``
      once corrected and approved.

    """
    item_type = models.CharField(
        max_length=256,
        verbose_name=_('Item group'),
    )

    value = models.CharField(
        max_length=4000,
        verbose_name=_('Value'),
    )

    is_user_generated = models.BooleanField(
        default=True,
        verbose_name=_('Is user generated'),
    )
