
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ReviewForm, projectForm
from .utils import searchProjects, paginateProjects



# Create your views here.

def projects(request):

    projects, search_content = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)

    context = {'projects':projects, 'search_content':search_content, 'custom_range':custom_range}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, 'review submitted successfully')
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', {'project': projectObj, 'form': form})


@login_required(login_url='login')
def createproject(request):
    profile = request.user.profile
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateproject(request, pk):
    profile = request.user.profile
    projectes = profile.project_set.get(id=pk)
    form = projectForm(instance=projectes)

    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES, instance=projectes)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete_template.html', context)

def about(request):
    return render(request, 'about.html')

def agents(request):
    return render(request, 'agents.html')

def team(request):
    return render(request, 'team-template.html')

def ComingSoon(request):
    return render(request, 'coming-soon.html')