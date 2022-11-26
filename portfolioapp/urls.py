from django.urls import path
from . import views
urlpatterns = [
    path("",views.projects, name="projects"),
    path("projects/<int:project_id>/",views.details , name="details"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact")
]