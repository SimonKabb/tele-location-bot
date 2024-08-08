from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('showmap/', include('showmap.urls')),
    path('admin/', admin.site.urls),
]
