from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import GenericModel
from .forms import GenericModelForm


class CreateGenericModelView(CreateView):
    model = GenericModel
    form_class = GenericModelForm
    template_name = 'generic_model/generic_model_create_form.html'
    success_url = reverse_lazy('gm:create_generic_model')
