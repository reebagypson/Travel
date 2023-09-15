from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='index'),
    path('oper/',views.oper,name='oper'),

]
