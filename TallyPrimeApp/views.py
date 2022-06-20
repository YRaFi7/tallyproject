from ast import Return
import re
from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def company(request):
    return render(request,'inventory_masters.html')

def stock_group(request):
    return render(request,'stock_group.html')

def stock_category_creation(request):
    return render(request,'stock_category_creation.html')

def unit_creation(requets):
    return render(requets,'unit_creation.html')

def godown_alteration(request):
    return render(request,'godown_alteration.html')

def employee_group_cretation(request):
    return render(request,'employee_group_cretation.html')

def employee_creation(request):
    return render(request,'employee_creation.html')
