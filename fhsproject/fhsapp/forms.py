from django import forms
from .models import Registration

class DateInput(forms.DateInput):
    input_type = "date"

class RegistrationForm(forms.ModelForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter full name"
    }))
    """gender = forms.ChoiceField(choices=Registration.gender_choices,widget=forms.TextInput(attrs={
        "class": "form-check-input",
        "placeholder": "select gender"
    }))"""
    dateofbirth = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "date",
        "placeholder": "enter dateofbirth"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter Email"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter Location"
    }))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "number",
        "placeholder": "enter Mobile No."
    }))



    class Meta:
        model = Registration
        fields = ['fullname','gender','dateofbirth','email','username','password','location','contact']    # it will display all the fields in the form except default fields like id and registrationtime
        widgets = {"password":forms.PasswordInput(),"dateofbirth":DateInput()}    # additional features of the fields
        labels = {"gender":"Select Gender","location":"Provide Location"}  #using this, we can change label name in the form
        exclude = {"gender"}       #using this, we can hide the fields in the form
