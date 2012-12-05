"""Forms for the ``django-crowdsourced-fields`` app."""
import json
import os

from django.conf import settings

from crowdsourced_fields.models import CrowdsourcedItem


def add_crowdsourced_values(cls, field_name, settings):
    """
    Dynamically adds a ``get_crowdsourced_values`` method to the form's fields.

    :cls: The form instance that should get the new method. Should be a formi
      instance with a model that has a ``CROWDSOURCED_FIELDS`` attribute.
    :field_name: The name of the original field.
    :settings: The dictionary with additional settings needed for adding the
      new method.

    """
    def inner_function(self):
        """
        The actual code of the function that returns the crowdsourced values.

        """
        this = inner_function
        this_name = this.__name__
        original_name = this_name.replace('_crowdsourced_values', '')
        model = self.__class__.Meta.model
        field_settings = model.CROWDSOURCED_FIELDS[original_name]
        items = list(CrowdsourcedItem.objects.filter(
            item_type=field_settings['item_type']).order_by(
                'value', ).values_list('value', flat=True))
        return json.dumps(items)

    inner_function.__doc__ = (
        'Returns the crowdsourced values for the {0} field'.format(
            field_name))
    inner_function.__name__ = '{0}_crowdsourced_values'.format(field_name)
    setattr(cls.__class__, inner_function.__name__, inner_function)


class CrowdsourcedFieldsFormMixin(object):
    class Media:
        css = {
            'all': (os.path.join(
                settings.STATIC_URL, 'crowdsourced_fields/css/combobox.css'), )
        }
        js = (
            os.path.join(
                settings.STATIC_URL, 'crowdsourced_fields/js/combobox.js', ),
        )

    def __init__(self, *args, **kwargs):
        super(CrowdsourcedFieldsFormMixin, self).__init__(*args, **kwargs)
        model = self.Meta.model
        for field_name, settings in model.CROWDSOURCED_FIELDS.items():
            add_crowdsourced_values(self, field_name, settings)
