from django.shortcuts import render
from .forms import MyForm, ApprovalForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib import messages
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
import keras

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


def ohevalue(df):
    ohe_col=['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Gender_Male',
       'Married_No', 'Married_Yes', 'Education_Graduate',
       'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
       'Property_Area_Rural', 'Property_Area_Semiurban',
       'Property_Area_Urban']
    cat_columns=['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']
    df_processed=pd.get_dummies(df, columns=cat_columns)
    new_dict={}
    for i in ohe_col:
        if i in df_processed.columns:
            new_dict[i]=df_processed[i].values
        else:
            new_dict[i]=0
    new_df=pd.DataFrame(new_dict)
    return new_df


# @api_view(["POST"])
def approvereject(unit):
    try:
        keras.backend.clear_session() # this is needed other wise we get an error - ValueError("Tensor %s is not an element of this graph." % obj)
        model_name = os.path.abspath(os.getcwd()).replace('\\', '/') + '/MLmodel/loan_madel.pkl'
        # print('start model loading')
        mdl = joblib.load(model_name)
        # print('end model loading')

        # # mydata=request.data
        # # unit=np.array(list(mydata.values()))
        # # unit=unit.reshape(1,-1)

        scaler_filename = os.path.abspath(os.getcwd()).replace('\\', '/') + '/MLmodel/scaler.pkl'
        # print('start scaler loading from {}'.format(scaler_filename))
        scalers = joblib.load(scaler_filename)
        # print('end scaler loading')
        # print('start scaling')
        X=scalers.transform(unit)
        # print('end scaling')
        X=unit
        # print('start predicting')
        y_pred=mdl.predict(X)
        # print('end predicting')
        # print('start filter')
        y_pred=(y_pred>0.58)
        # print('end filter')
        # print("y_pred = {}".format(y_pred))
        newdf=pd.DataFrame(y_pred, columns=['Status'])
        newdf=newdf.replace({True:'Approved', False:'Rejected'})
        # print(newdf)
        # return JsonResponse('Your Status is {}'.format(newdf), safe=False)
        return ('Your status is {}'.format(newdf.values[0][0]))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def custcontact(request):
    if request.method=='POST':
        form=ApprovalForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            Dependents=form.cleaned_data['Dependents']
            ApplicantIncome=form.cleaned_data['ApplicantIncome']
            CoapplicantIncome=form.cleaned_data['CoapplicantIncome']
            LoanAmount=form.cleaned_data['LoanAmount']
            Loan_Amount_Term=form.cleaned_data['Loan_Amount_Term']
            Credit_History=form.cleaned_data['Credit_History']
            Gender=form.cleaned_data['Gender']
            Married=form.cleaned_data['Married']
            Education=form.cleaned_data['Education']
            Self_Employed=form.cleaned_data['Self_Employed']
            Property_Area=form.cleaned_data['Property_Area']
            myDict=(request.POST).dict() # need to understand this part
            df=pd.DataFrame(myDict, index=[0])
            # print('x')
            answer = (approvereject(ohevalue(df))) # this is just a function that takes df as input and gives result of approval/rejection
            messages.success(request, 'Application status: {}'.format(answer))
            # print('x')
            print(firstname, lastname, Dependents, Married, Property_Area)
    
    form=ApprovalForm()

    return render(request, 'myform/form.html', {'form':form})
