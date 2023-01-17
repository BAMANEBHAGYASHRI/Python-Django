from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hellooo Djangooo !!")

def home(request):
    return HttpResponse("hellooo web devloper")


def january(request):
    return HttpResponse("happy new year !")

def febrbuary(request):
    return HttpResponse("Birth day of cha.shivaji maharaj !")

# def home(request):
#     return render(request,'home.html',{'name':'ADCET'})
