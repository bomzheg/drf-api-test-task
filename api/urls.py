from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^api/', include('polls.urls')),
    path(r'admin/', admin.site.urls),
]
