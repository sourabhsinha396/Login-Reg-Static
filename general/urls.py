

from django.urls import path,include
from .views import contactus,login_page,register_page,homepage

app_name = 'general'

urlpatterns = [
	path('contact/',contactus,name="contact"),
	path('login/',login_page,name="login"),
	path('register/',register_page,name="register"),

]
