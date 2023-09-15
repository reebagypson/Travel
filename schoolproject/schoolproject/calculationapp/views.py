from django.shortcuts import render

def oper(request):
    firstnumber=int(request.GET['num1'])
    secondnumber=int(request.GET['num2'])
    a=firstnumber+secondnumber
    b=firstnumber-secondnumber
    c=firstnumber*secondnumber
    d=firstnumber/secondnumber
    return render(request,"result.html",{'Add':a,'Sub':b,'Mul':c,'Div':d})

def home(request):
    return render(request,"home.html")

