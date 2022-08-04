from django.urls import path
from . import views

urlpatterns = [ 
    path("employee/", views.Employee.as_view()),
    path("get/",views.get.as_view())
]
