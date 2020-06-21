from django.forms import ModelForm
from .models import Approvals
from django import forms

class MyForm(ModelForm):
    class Meta:
        model=Approvals
        fields='__all__'

class ApprovalForm(forms.Form):
    firstname = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter firstname'}))
    lastname = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter lastname'}))
    Dependents = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter number of dependents'}))
    ApplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter mosthly gross income'}))
    CoapplicantIncome = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter co-applicant monthly gross income'}))
    LoanAmount = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested loan amount'}))
    Loan_Amount_Term = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan term in months'}))
    Credit_History = forms.ChoiceField(choices=[('1', 1), ('0', 0)])
    Gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    Married = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Education = forms.ChoiceField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')])
    Self_Employed = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    Property_Area = forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])