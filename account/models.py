

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self,email,fullname,password,is_active=True,is_staff=False,is_superuser=False):
        if not email:
            raise ValueError("You must specify an email")

        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.fullname=fullname
        user.is_active=is_active
        user.is_staff=is_staff
        user.is_superuser=is_superuser
        user.save(using=self.db)
        return user

    def create_staffuser(self,email,password,fullname):
        user=self.create_user(email=email,password=password,fullname=fullname,is_staff=True)
        return user

    def create_superuser(self,email,password,fullname):
        user=self.create_user(email=email,password=password,fullname=fullname,is_staff=True,is_superuser=True)
        return user


def user_profile_dir(instance,filename):
    return f'profile_pictures/{instance.email}/{filename}'
    

class User(AbstractBaseUser,PermissionsMixin):
    email=models.CharField(max_length=200,unique=True)
    fullname=models.CharField(max_length=200)
    
    
    profile_picture=models.ImageField(upload_to=user_profile_dir,null=True,blank=True,default=None)

    ot_token=models.CharField(max_length=60,blank=True,null=True,default=None)
    is_active=models.BooleanField()
    is_staff=models.BooleanField()

    



    def ot_token_set_expire(self):
        self.ot_token=None

        self.save()

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['fullname']
    objects=UserManager()



