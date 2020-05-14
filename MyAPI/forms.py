from django.forms import ModelForm
from .models import Approvals
from django import forms

class MyForm(ModelForm):
    class Meta:
        model=Approvals
        fields='__all__'

class ApprovalForm(forms.Form):
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    Dependents = forms.IntegerField()
    ApplicantIncome = forms.IntegerField()
    CoapplicantIncome = forms.IntegerField()
    LoanAmount = forms.IntegerField()
    Loan_Amount_Term = forms.IntegerField()
    Credit_History = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Education = forms.ChoiceField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')])
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])