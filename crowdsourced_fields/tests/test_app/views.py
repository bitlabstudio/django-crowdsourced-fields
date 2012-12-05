"""Test view for the `django-user-tags` app."""
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from crowdsourced_fields.tests.test_app.forms import DummyModelForm
from crowdsourced_fields.tests.test_app.models import DummyModel


class TestView(FormView):
    template_name = 'test_app/test_view.html'
    form_class = DummyModelForm

    def form_valid(self, form):
        form.save()
        return super(TestView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(TestView, self).get_context_data(**kwargs)
        ctx.update({'objects': DummyModel.objects.all(), })
        return ctx

    def get_success_url(self):
        return reverse('crowdsourced_fields_test_view')


class TestDetailView(TestView):
    def get_form_kwargs(self):
        kwargs = super(TestDetailView, self).get_form_kwargs()
        kwargs.update({
            'instance': DummyModel.objects.get(pk=self.kwargs.get('id'))
        })
        return kwargs
