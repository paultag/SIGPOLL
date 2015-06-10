from django.conf.urls import include, url
from django.contrib import admin
import sigpoll.urls

urlpatterns = [
    url(r'^', include(sigpoll.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
