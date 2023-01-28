from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("<int:day>",views.challanges_byNumber),
    path("<str:day>",views.challanges,name="days_challanges")
]