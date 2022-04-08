from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Department

# Create your views here.

def departments(request):
    all_departments = Department.objects.all()
    context = {
        'all_departments': all_departments
    }
    return  render(request, "index.html", context)

