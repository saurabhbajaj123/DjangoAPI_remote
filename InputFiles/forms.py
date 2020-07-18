from django import forms
from . import views
from django.contrib.auth.forms import UserCreationForm

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=500)
    file = forms.FileField(required=False)

class UserCreationForm(forms.Form):

    # this init function contians the field which we want to shaow in the form.
    # Here even if we dont give the choices argument, it'll work
    # this code is a little more flexible, it can take arguments in the init funciton, but it 
    # was giving an error, so dynamic allocation of choices is done in the views.py
    # using - form.fields['Columns'].choices = getChoices(columns)
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['Columns'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])


    # Another way of doing the same thing as above
    # Columns = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)