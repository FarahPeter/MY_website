from django.shortcuts import render, redirect
from .forms import ImageNameForm, LinkForm, AboutForm, EducationForm, ExperienceForm, ProjectForm, CertificateTestForm, SkillForm

def upload_image_name(request):
    if request.method == 'POST':
        form = ImageNameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageNameForm()
    return render(request, 'upload_image_name.html', {'form': form})

def upload_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = LinkForm()
    return render(request, 'upload_link.html', {'form': form})

def upload_about(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AboutForm()
    return render(request, 'upload_about.html', {'form': form})

def upload_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EducationForm()
    return render(request, 'upload_education.html', {'form': form})

def upload_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ExperienceForm()
    return render(request, 'upload_experience.html', {'form': form})

def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProjectForm()
    return render(request, 'upload_project.html', {'form': form})

def upload_certificate_test(request):
    if request.method == 'POST':
        form = CertificateTestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CertificateTestForm()
    return render(request, 'upload_certificate_test.html', {'form': form})

def upload_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SkillForm()
    return render(request, 'upload_skill.html', {'form': form})

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from .models import ImageName, Link, About, Education, Experience, Project, CertificateTest, Skill

def home(request):
    image_name = ImageName.objects.first()
    links = Link.objects.all()
    about = About.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Project.objects.all()
    certificates = CertificateTest.objects.all()
    skills = Skill.objects.all()
    context = {
        'image_name': image_name,
        'links': links,
        'about': about,
        'education': education,
        'experience': experience,
        'projects': projects,
        'certificates': certificates,
        'skills': skills,
    }
    return render(request, 'home.html', context)

