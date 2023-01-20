from django.urls import path
from . import views
urlpatterns=[
    # path("index",views.index,name="index"),
    # path("home",views.home,name="home"),
    # path("",views.january,name="january"),
    # path("febrbuary",views.febrbuary,name="febrbuary"),

    path("<month>",views.monthly_challanges)
    
]