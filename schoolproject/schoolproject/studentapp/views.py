from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# def Home(request):
#     return HttpResponse("helloworld")
def about(request):
    name='Gipson'
    return render(request,"about.html",{'obj':name})
# def Contacts(request):
#     return render(request,'contacts.html')
# def Details(request):
#     return render(request,'details.html')
# def Thanks(request):
#     return HttpResponse("Thanks")
def addition(request):
    firstnumber=int(request.GET['num1'])
    secondnumber=int(request.GET['num2'])
    res=firstnumber+secondnumber
    return render(request,"result.html",{'result':res})
