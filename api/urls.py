from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^api/', include('pools.urls')),
    path(r'admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]
