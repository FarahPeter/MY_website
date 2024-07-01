from django.contrib import admin
from django.urls import path, include
from .views import home, upload_image_name, upload_link, upload_about, upload_education, upload_experience, upload_project, upload_certificate_test, upload_skill, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('upload/image-name/', upload_image_name, name='upload_image_name'),
    path('upload/link/', upload_link, name='upload_link'),
    path('upload/about/', upload_about, name='upload_about'),
    path('upload/education/', upload_education, name='upload_education'),
    path('upload/experience/', upload_experience, name='upload_experience'),
    path('upload/project/', upload_project, name='upload_project'),
    path('upload/certificate-test/', upload_certificate_test, name='upload_certificate_test'),
    path('upload/skill/', upload_skill, name='upload_skill'),
    path('success/', success, name='success'),
]
