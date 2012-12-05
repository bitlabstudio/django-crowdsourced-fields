"""Models of the ``django-crowdsourced-fields`` app."""
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


def add_crowdsourced_method(cls, field_name, settings):
    """
    Dynamically adds a ``fieldname_crowdsourced`` method to an object.

    :cls: The object that should get the new method. Should be a model instance
      and should have a ``CROWDSOURCED_FIELDS`` attribute.
    :field_name: The name of the original field.
    :settings: The dictionary with additional settings needed for adding the
      new method.

    """
    def inner_function(self):
        """
        The actual code of the function that returns the crowdsourced value.

        """
        this = inner_function
        this_name = this.__name__
        original_name = this_name.replace('_crowdsourced', '')
        field_settings = self.CROWDSOURCED_FIELDS[original_name]
        content_type = ContentType.objects.get_for_model(self)
        fk = CrowdsourcedItemGenericForeignKey.objects.get(
            content_type=content_type, object_id=self.pk,
            item_type=field_settings['item_type'])
        return fk.item.value

    inner_function.__doc__ = (
        'Returns the crowdsourced value for the {0} field'.format(
            field_name))
    inner_function.__name__ = '{0}_crowdsourced'.format(field_name)
    setattr(cls.__class__, inner_function.__name__, inner_function)


class CrowdsourcedFieldsModelMixin(object):
    """
    Adds ``fieldname_crowdsourced`` methods to the class.

    In order to use this mixin, please add a ``CROWDSOURCED_FIELDS`` attribute
    to your model class. See README for further instructions.

    Instead of displaying the real field in your templates, you should always
    display the crowdsourced value instead.

    """
    def __init__(self, *args, **kwargs):
        super(CrowdsourcedFieldsModelMixin, self).__init__(*args, **kwargs)
        for field_name, field_settings in self.CROWDSOURCED_FIELDS.items():
            add_crowdsourced_method(self, field_name, field_settings)


class CrowdsourcedItemGenericForeignKey(models.Model):
    """
    Maps ``CrowdsourcedItem`` objects to the objects that use them.

    This is a workaround because we don't want to dynamically add foreign
    keys to the objects that have crowdsourced fields. We use this mapping
    relationship instead to remember which object/field belongs to which
    ``CrowdsourcedItem``.

    :content_type: Part of the generic foreign key to the object this object
      belongs to.
    :object_id: See ``content_type``
    :content_object: See ``content_type``
    :item: The crowdsourced item which holds the approved data.
    :item_type: We need this in order to know which ``CrowdsourcedItem`` to
      get.

    """
    class Meta:
        unique_together = ('object_id', 'item_type', )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    item = models.ForeignKey(
        'crowdsourced_fields.CrowdsourcedItem',
    )

    item_type = models.CharField(
        max_length=256,
        verbose_name=_('Item group'),
    )



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
