from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.


def projects(request):

    latest_projects = Project.objects.order_by("-date")
    return render(
        request, "portoflioapp/projects.html", {"latest_projects": latest_projects}
    )

    


def details(request, project_id):

    project = Project.objects.get(pk=project_id)
    project_skills = project.skills.all()
    project_images = project.imgs.all()
    return render(request, "portoflioapp/details.html", {"project": project,"project_skills":project_skills,"project_images":project_images})
