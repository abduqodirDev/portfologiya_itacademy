from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Review, Comment
from django.contrib.auth.models import User
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects=Project.objects.all()
    context={
        "projects":projects
        }
    return render(request, "projects.html", context)

def project(request, id):
    try:
        project=Project.objects.get(id=id)
    except:
        messages.warning(request, "bunaqa loyiha topilmadi")
        return redirect("projects")
    tags=project.tag.all()
    comments = Comment.objects.filter(project=project)
    if request.method=="POST":
        users=User.objects.all()  
        if request.user not in  users:
            messages.warning(request, "comment yozish uchun avval tizimga kirishingiz kerak")
            return redirect("login")
        message = request.POST["comment"]
        Comment.objects.create(project=project, user=request.user.profile, body=message)
    context={
        "project":project,
        "tags":tags,
        "comments":comments
        }
    return render(request, "project.html", context)

@login_required(login_url="login")
def project_add(request):
    if request.method=="POST":
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user.profile
            project.save()
            return redirect('projects')
    form=ProjectForm()
    context={
        "form":form
        }
    return render(request, "project_add.html", context)

@login_required(login_url="login")
def project_edit(request, id):
    project=Project.objects.get(id=id)
    if not project.user == request.user.profile:
        messages.warning(request, "o'zingizdan tashqari loyihani o'zgartira ololmaysiz")
        return redirect("profiles")
    form=ProjectForm(instance=project)
    if request.method=="POST":
        form=ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={
        "form":form
        }
    return render(request, "project_add.html", context)

@login_required(login_url="login")
def project_delete(request, id):
    project=Project.objects.get(id=id)
    if not project.user == request.user.profile:
        messages.warning(request, "o'zingizdan tashqari loyihani o'zgartira ololmaysiz")
        return redirect("profiles")
    project.delete()
    return redirect("projects")

def search_result(request):
    text = request.GET["text"]
    search_result = Project.objects.filter(title__icontains=text)
    context = {
        "projects":search_result
        }
    
    return render(request, "search/search_result_project.html", context)


