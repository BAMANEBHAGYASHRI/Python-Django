from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("This works !")

weekly_challanges = {
    "sunday":"happy sunday",
    "monday":"happy monday",
    "tuesday":"happy tuesday",
    "wensday":"happy wendsday",
    "thursday":"happy thrusday",
    "friday":"hapy friday",
    "staurday":"happy saturdayy"
}

def index(request):
    list_item=""
    days=list(weekly_challanges.keys())
    for day in days:
        capitalized_days=day.capitalize()
        day_path=reverse("days_challanges",args=[day])
        list_item+= f"<li><a href=\"{day_path}\">{capitalized_days}</a></li>"

    response_data=f"<ul>{list_item}</ul>"
    return HttpResponse(response_data)









def challanges_byNumber(request,day):
    days=list(weekly_challanges.keys())
    if day > len(days):
        return HttpResponseNotFound("invalud daysssssss")
    redirect_day=days[day - 1]
    redirect_path=reverse("days_challanges",args=[redirect_day])
    return HttpResponseRedirect(redirect_path)

def challanges(request,day):
    try:
        text=weekly_challanges[day]
        response_data=f"<h2>{text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("this weeks is not supported!")
    
   