from django import forms
from .models import RegisterMForm




class LoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
	


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model=RegisterMForm
        fields=['Username','Email','Password','Confirm_Password']
        widgets = {
          'Email':forms.TextInput(attrs={"class":"form-control"}),
          'Username':forms.TextInput(attrs={"class":"form-control"}),
          'Confirm_Password':forms.TextInput(attrs={"class":"form-control"}),
          'Password':forms.PasswordInput(attrs={"class":"form-control"})
          }