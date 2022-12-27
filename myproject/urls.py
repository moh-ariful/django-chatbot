from django.contrib import admin
from django.urls import path
from landingpage.views import index, generate_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("generate-text/", generate_text, name="generate_text"),
]
