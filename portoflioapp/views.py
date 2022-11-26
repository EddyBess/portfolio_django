from django.shortcuts import render
from django.http import HttpResponse

from .models import Project
# Create your views here.
def projects(request):
    latest_projects = Project.objects.order_by('-date')[:3]
    
    return render(request, "portoflioapp/projects.html",{
        "latest_projects" : latest_projects 
        })

def details(request , project_id):
    project = Project.objects.get(pk = project_id)
    return render(request , "portoflioapp/details.html",{
        "project":project
    })