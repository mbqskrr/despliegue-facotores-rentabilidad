from django.shortcuts import render
#from django.http import HttpResponse

def Swiset(request):
    #return HttpResponse("Hello world")
    return render(request, "Swiset.html")

# Create your views here.
