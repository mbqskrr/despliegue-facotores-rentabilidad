from django.shortcuts import render
import joblib 
import numpy as np
from sklearn.preprocessing import PolynomialFeatures


#from django.http import HttpResponse

def Swiset(request):
    #return HttpResponse("Hello world")
    return render(request, "Swiset.html")

def Result(request):
    
    cls = joblib.load("model.sav")

    list = []
    list.append(request.GET['entry'])
    list.append(request.GET['close'])
    list.append(request.GET['sl'])
    list.append(request.GET['vpip'])
    list.append(request.GET['porcentaje'])
    list.append(request.GET['monetario'])
    list.append(request.GET['commisions'])
    list.append(request.GET['asset'])
    list.append(request.GET['broker'])
    list.append(0)
   
    list_f = [float(i) for i in list]

    #poly = PolynomialFeatures(degree=2)
    #list_f = poly.fit_transform(list_f)

    vct = np.array(list_f)

    #new_vct = vct.reshape(1,-1) 
    
    ans = cls.predict([vct])
   
    return render(request, "Result.html", {'ans':ans})
