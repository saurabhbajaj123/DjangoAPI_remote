from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import UploadFileForm, UserCreationForm
import json
import csv, io, codecs, re
import pandas as pd
# import papaparse as Papa
# Create your views here.
columns = []
def upload_file(request):
    if request.method == 'POST':
        print('1')
        # uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        form = UploadFileForm(request.POST, request.FILES) # did not understood the 
        print('2')
        print(form.is_valid())
        if form.is_valid():
            print('2.5')
            uploaded_file = request.FILES['file']

            print(uploaded_file.name)
            print(uploaded_file.size)

            print('reading csv into pandas')
            df = pd.read_csv(uploaded_file)
            print(df.head())
            columns = df.columns
            print(columns)

            # creating a filesystem object to save file
            # defines the location where the files will be stored
            fs = FileSystemStorage(location=settings.UPLOAD_ROOT, base_url=settings.UPLOADED_URL)
            # to see the file in the browser, check - http://127.0.0.1:8000/<UPLOADED_URL>/<file name>
            # fs.save(uploaded_file.name, uploaded_file)
            print('2.9')
            return render(request, 'upload_forms/upload.html', {'form': form})
    else:
        print('3')
        form = UploadFileForm()
    return render(request, 'upload_forms/upload.html', {'form': form})
    # return render(request, 'upload_forms/upload.html')


def multiple_choices(request):
    columns = ['id', 'packages_required', 'pakcages_installed', 'exactly']
    def getChoices(list_):    
        list_column_tuples = []
        for i in zip(list_, list_):
            list_column_tuples.append(i)
        OPTIONS = tuple(list_column_tuples)
        return OPTIONS
    print(getChoices(columns))
    if request.method == 'POST':
        print('request.method == POST')
        print(request)
        form = UserCreationForm(request.POST)
        # below is where we are assigning the values to be shown in 
        # form, although in some places it is written that this is not
        # a good way to assign the values
        form.fields['Columns'].choices = getChoices(columns) 
        print(request.POST)
        columns_dict = request.POST.getlist("Columns")
        print(columns_dict)
        print('form created')
        # print(form)
        # print(form2.errors)
        if form.is_valid():
            print('form is valid')
        #     columns = form2.cleaned_data.get('Columns')
        #     print(columns) # {'Columns': ['id', 'packages_required', 'pakcages_installed']}
    else:
        print('response method is not post')
        form = UserCreationForm()
        # Here we give the values for the first look of the form
        form.fields['Columns'].choices = getChoices(columns) 

    return render(request, 'upload_forms/upload.html', {'form': form})


