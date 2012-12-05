from django import forms

from crowdsourced_fields.forms import CrowdsourcedFieldsFormMixin
from crowdsourced_fields.tests.test_app.models import DummyModel


class DummyModelForm(CrowdsourcedFieldsFormMixin, forms.ModelForm):
    """We need this to test the ``CrowdsourcedFieldsFormMixin``."""
    class Meta:
        model = DummyModel

    def __init__(self, user=None, *args, **kwargs):
        if user is not None:
            self.user = user
        super(DummyModelForm, self).__init__(*args, **kwargs)
