from django.shortcuts import render

# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('report/data', views.capacitidata_report_page, name='Data_report'),
    path('report/Activities', views.Activities_report_page, name='Activities_report'),
]

from django.shortcuts import render


def capacitidata_report_page(request):
   return render(request, 'dashboard.html', {})


def Activities_report_page(request):
   return render(request, 'Activities_report.html', {})