from django import forms
from . import views
from django.contrib.auth.forms import UserCreationForm

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=500)
    file = forms.FileField(required=False)

class UserCreationForm(forms.Form):
    columns = ['id', 'packages_required', 'pakcages_installed', 'exactly']

    # def __init__(self, *args, **kwargs):
    #     extra = kwargs.pop('extra')
    #     super(UserCreationForm, self).__init__(*args, **kwargs)
    #     self.columns = extra
    
    def getChoices(list_):    
        list_column_tuples = []
        for i in zip(list_, list_):
            list_column_tuples.append(i)
        OPTIONS = tuple(list_column_tuples)
        return OPTIONS
    Columns = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, 
                                          choices=getChoices(columns))