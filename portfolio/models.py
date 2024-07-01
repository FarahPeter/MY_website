from django.db import models

class ImageName(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)

class Link(models.Model):
    LINK_TYPE_CHOICES = [
        ('LinkedIn', 'LinkedIn'),
        ('GitHub', 'GitHub'),
    ]
    link_type = models.CharField(max_length=50, choices=LINK_TYPE_CHOICES)
    url = models.URLField(max_length=255)

class About(models.Model):
    content = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    supporting_files = models.FileField(upload_to='education/', null=True, blank=True)

class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    supporting_files = models.FileField(upload_to='experience/', null=True, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    supporting_files = models.FileField(upload_to='projects/', null=True, blank=True)

class CertificateTest(models.Model):
    title = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    date_issued = models.DateField()
    supporting_files = models.FileField(upload_to='certificates/', null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, null=True, blank=True)
