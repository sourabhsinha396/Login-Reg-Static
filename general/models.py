from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Create your models here.
class RegisterMForm(models.Model):
    Username = models.CharField(max_length=140,blank=False)
    Email= models.EmailField(max_length=120,blank=True)
    Password=models.CharField(max_length=50,blank=False)
    Confirm_Password=models.CharField(max_length=50,blank=False)


    def clean(self,*args,**kwargs):
        pass1 = self.Password
        pass2 = self.Confirm_Password
        if pass1 != pass2:
            raise ValidationError("Passwords must Match ")

        #username validation
        username=self.Username
        if User.objects.filter(username=self.Username).exists():
            raise ValidationError(" User already Existss")
        return super(RegisterMForm,self).clean(*args,**kwargs)