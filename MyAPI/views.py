from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Approvals
from .serializers import approvalsSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.http import HttpResponse
import os

# def index(request):
#     return HttpResponse("Hello, world. You're at the MyAPI index.")

# Create your views here.
class ApprovalsView(viewsets.ModelViewSet):
    queryset = Approvals.objects.all()
    serializer_class = approvalsSerializers

def myform(request):
    if request.method=="POST":
        form = MyForm(request.POST)
        if form.is_valid():
            myform  = form.save(commit=False)
    else:
        form = MyForm()

@api_view(["POST"])
def approvereject(request):
    try:
        model_name = os.path.abspath(os.path.join(os.getcwd(), os.pardir)).replace('\\', '/') + '/loan_madel.pkl'
        mdl = joblib.load(model_name)
        mydata=request.data
        unit=np.array(list(mydata.values()))
        unit=unit.reshape(1,-1)
        scaler_filename = os.path.abspath(os.path.join(os.getcwd(), os.pardir)).replace('\\', '/') + '/scaler.pkl'
        scalers=joblib.load(scaler_filename)
        X=scalers.transform(unit)
        y_pred=mdl.predict(X)
        y_pred=(y_pred>0.58)
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        newdf=newdf.replace({True:'Approved', False:'Rejected'})
        return JsonResponse('Your Status is {}'.format(newdf), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

