from django.conf.urls import url

from . import views

app_name = 'pools'

urlpatterns = [
    url(r'pools/', views.PoolsView.as_view(), name='pools'),
]
