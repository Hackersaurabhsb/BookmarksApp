from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile
from PIL import Image
#--------------------------------------------------------------------------------#
#form for user deletion process
class delete_account(forms.Form):
        email=forms.EmailField()
#--------------------------------------------------------------------------------#
#
#
#----------------------------------------------------------------------------------#
#form for user registration
class user_registration_form(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username","first_name","email"]
        User.is_superuser=False
        User.is_staff=False
        User.username.unique=True
    def clean_password2(self):
        #Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    def clean_email(self):
        data=self.cleaned_data['email']
        print(data)
        if User.objects.filter(email=data).exists():
            print(User.objects.filter(email=data).exists())
            raise forms.ValidationError("Email already exists")
        return data
#--------------------------------------------------------------------------------#
#
#
#---------------------------------------------------------------------------------#
#form to edit users
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
    def clean_email(self):
        datas=self.cleaned_data['email']
        query_set=User.objects.exclude(id=self.instance.id).filter(email=datas)
        if query_set.exists():
            raise ValidationError("Email is already in use")
        return datas
#-------------------------------------------------------------------------------#
#
#
#--------------------------------------------------------------------------------# 
#form to edit profile related to user
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['date_of_birth','photo']

#--------------------------------------------------------------------------------#

#form to edit profile pic of users
class Profile_pic_change(forms.Form):
    image=forms.ImageField()

    
