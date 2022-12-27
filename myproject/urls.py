from django.contrib import admin
from django.urls import path
from landingpage.views import index, about_view, generate_konten, generate_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("about/", about_view, name="about"),
    path("generate/", generate_konten, name="generate-konten"),
    path("generate-text/", generate_text, name="generate_text"),
]
