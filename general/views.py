from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterModelForm


#login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model
# Create your views here.

def homepage(request):
	return redirect('/general/contact/')

def contactus(request):
	if request.method=='POST':
		print(request.POST)
		print(request.POST.get('fullname'))
	return render(request,'general/contactus.html',{'Title':'Contacttt US'})



def login_page(request):
	form=LoginForm(request.POST or None)
	context={'form':form}
	if request.user.is_authenticated :
		logdict={'message':'{} already logged in'.format(request.user),
		'form':form,
		'premium':'premium',}
		return render(request,'auth/login.html',logdict)

	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect("/general/login/")
		else:
			print("error")
	return render(request,"auth/login.html",context)



User=get_user_model()
def register_page(request):
	form=RegisterModelForm(request.POST or None)
	context={'form':form}
	if form.is_valid():
		username=form.cleaned_data.get('Username')
		password=form.cleaned_data.get('Password')
		email=form.cleaned_data.get('Email')
		new_user=User.objects.create_user(username,email,password)
		print(new_user)
		print(form.cleaned_data)
	return render(request,"auth/register.html",{'Titlebody':"login",'form':form})


