from django import forms
from .models import ImageName, Link, About, Education, Experience, Project, CertificateTest, Skill

class ImageNameForm(forms.ModelForm):
    class Meta:
        model = ImageName
        fields = ['image', 'name']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link_type', 'url']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['content']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date', 'supporting_files']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job_title', 'company', 'start_date', 'end_date', 'supporting_files']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'supporting_files']

class CertificateTestForm(forms.ModelForm):
    class Meta:
        model = CertificateTest
        fields = ['title', 'issuing_organization', 'date_issued', 'supporting_files']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']
