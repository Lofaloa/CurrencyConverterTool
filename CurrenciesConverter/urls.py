from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('converter/', include('converter.urls')),
    path('admin/', admin.site.urls),
]
