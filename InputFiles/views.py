from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        print('1')
        # uploaded_file = request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        form = UploadFileForm(request.POST, request.FILES) # did not understood the part
        print('2')
        print(form.is_valid())
        if form.is_valid():
            print('2.5')

            uploaded_file = request.FILES['file']
            print(uploaded_file.name)
            print(uploaded_file.size)
            print('2.9')
            return render(request, 'upload_forms/upload.html', {'form': form})
        
    else:
        print('3')
        form = UploadFileForm()
    return render(request, 'upload_forms/upload.html', {'form': form})
    # return render(request, 'upload_forms/upload.html')


