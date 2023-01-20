from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

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


# Dynamic path segments and captued values
def monthly_challanges(reuqest,month):
    challanges_text=None
    if month=="january":
        challanges_text="happy new year"
    elif month=="febrbuary":
        challanges_text="Birth day of cha.shivaji maharaj !"
    elif month=="march":
        challanges_text="happy holi !"
    else:
        return HttpResponseNotFound
    return HttpResponse(challanges_text)