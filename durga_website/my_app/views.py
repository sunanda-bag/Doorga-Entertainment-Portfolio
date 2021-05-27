from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html',context)

def shuga_magazine(request):
    context = {}
    return render(request,'shuga_magazine.html',context)

def ary_world(request):
    context = {}
    return render(request,'ary_world.html',context)

def mission(request):
    context = {}
    return render(request,'mission.html',context)

def pricing(request):
    context = {}
    return render(request,'pricing.html',context)
