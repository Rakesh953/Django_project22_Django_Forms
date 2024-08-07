from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse


# Create your views here.
def djangoForm(request):
    ESTFO=StudentForm()
    d={'ESTFO':ESTFO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('Invalid Data') 

    return render(request,'djangoForm.html',d)