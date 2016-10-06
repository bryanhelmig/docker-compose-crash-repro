from django.conf.urls import include, url
from django.contrib import admin

from .views import HeavyView

urlpatterns = [
    url(r'^$', HeavyView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
