from django.conf.urls import url

from .views import CreateGenericModelView


app_name = 'generic_model'
urlpatterns = [
    url('^add$', CreateGenericModelView.as_view(), name='create_generic_model'),
]
