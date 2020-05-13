from django.contrib import admin
from django.urls import include, path

web_urlpatterns = [
    path('', include('web.urls')),
]

urlpatterns = [
    path('', include(web_urlpatterns)),
    path('admin/', admin.site.urls),
]
