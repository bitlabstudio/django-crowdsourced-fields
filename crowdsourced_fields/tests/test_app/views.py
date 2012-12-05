"""Test view for the `django-user-tags` app."""
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from crowdsourced_fields.tests.test_app.forms import DummyModelForm


class TestView(FormView):
    template_name = 'test_app/test_view.html'
    form_class = DummyModelForm

    def get_success_url(self):
        return reverse('crowdsourced_fields_test_view')
