from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hellooo Djangooo !!")

def home(request):
    return HttpResponse("hellooo web devloper")

# def home(request):
#     return render(request,'home.html',{'name':'ADCET'})
