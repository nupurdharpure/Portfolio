from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
        path('certificate/<int:certificate_id>/', views.certificate_detail, name='certificate_detail'),

]

