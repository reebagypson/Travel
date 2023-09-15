from . import views
from django.urls import path

urlpatterns = [
    # path('',views.Home,name='home'),
    path('',views.about,name='about'),
    # path('contacts/',views.Contacts,name='contacts'),
    # path('details/',views.Details,name='details'),
    # path('thanks/',views.Thanks,name='Thanks'),
    #path('add/',views.addition,name='addition')
]
