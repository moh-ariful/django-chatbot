from django.contrib import admin
from django.urls import path
from landingpage.views import index, diskusi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("diskusi/", diskusi, name="diskusi"),
]
