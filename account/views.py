from django.shortcuts import render
from .forms import user_registration_form,delete_account,UserEditForm,ProfileEditForm,Profile_pic_change
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect
from django.contrib import messages
from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
#here i have to create default login and logout views
######################################################################
############################------PRO TIP---------####################
# we can show validation just by managing return render lines 
# Create your views here.
def process_login_form(request):
    pass
        
# login required decorator 
#The login_required decorator checks if the current user is 
#authenticated. If the user is authenticated, it executes the decorated view; if the user 
#is not authenticated, it redirects him to the login URL with the URL he was trying to 
#access as a GET parameter named next. By doing so, the log in view redirects the user 
#back to the URL he was trying to access after he is successfully logged in. Remember 
#that we added a hidden input in the form of our log in template for this purpose.
@login_required
def dashboard(request):
    return render(request,"dashboard.html",{'section':'dashboard'})
#def sending_mail(request):
 #   send=send_mail("this is the subjectd","Someone has requested for your password reset",, recipient_list)
def register(request):
    if request.method=="POST":
        user_form=user_registration_form(data=request.POST)
        if user_form.is_valid():
            cd=user_form.cleaned_data
            #create a new user but for now don't save it
            new_user=user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(cd['password2'])
            new_user.save()
            #create user profiles
            Profile.objects.create(user=new_user)
            if new_user.profile.photo:
                print("inside the profile if condition ")
                return new_user.profile.photo.url
            else:
                #setattr(new_user,Profile.photo,"pngwing.png")
                print("Please select your photo ")
            return render(request,"register_done.html",{'user_form':user_form})
    else:
        user_form=user_registration_form()
    return render(request,"register.html",{'user_form':user_form})


#custom delete view 
def delete_account_user(request):
    print("executing")
    if request.method=="POST":
        print("INSIDE FIRST ELSE")
        delete=delete_account(request.POST)
        if delete.is_valid():
            print("inside valid condition")
            cd=delete.cleaned_data
            email_user=cd['email']
            try:
                user=User.objects.get(email=email_user)
            except MultipleObjectsReturned:
                raise forms.ValidationError("Unable to verify, please try again later")
                return render(request,"delete_account.html",{"form":delete})
            user.delete()
            return render(request,"delete_account_done.html",{"form":delete})
    else:
        delete=delete_account()
        return render(request,"delete_account.html",{"form":delete})



#view to process after user deletion
def delete_done(request):
    return render(request,"delete_account_done.html")

#this is view is for profile model related to the user model
@login_required
def edit(request):
    if request.method=="POST":
        user_edit_form=UserEditForm(instance=request.user,data=request.POST)
        profile_edit_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect("dashboard")
    else:
        user_edit_form=UserEditForm(instance=request.user)
        profile_edit_form=ProfileEditForm(instance=request.user.profile)
    return render(request,"edit.html",{"user_form":user_edit_form,"profile_form":profile_edit_form})




def settings(request):
    pass



#The messages framework includes the context processor django.contrib.messages.context_
#processors.messages, which adds a messages variable to the request context. You can find it in the 
#context_processors list in the TEMPLATES setting of your project. You can use the messages variable 
#in templates to display all existing messages to the user
#A context processor is a Python function that takes the request object as an argument and 
#returns a dictionary that gets added to the request context.


def profile_pic_view(request):
    print("executing the function")
    if request.method=='POST':
        print("executed")
        pic_instance=Profile_pic_change(request.POST)
        if pic_instance.is_valid():
            print("inside valid condition")
            cd=pic_instance.cleaned_data
            print(pic_instance.cleaned_data)
            print(cd['image'])
            img=cd['image']
            print(request.user.profile.photo)
            #request.user.profile.photo.url=cd['image']
            messages.success(request,"Profile pic changed successfully")
            return redirect("dashboard")
    else:
        pic_instance=Profile_pic_change()
    return render(request,"profile_pic_change.html",{"form":pic_instance})

#the below view is to show list of peoples
@login_required
def user_list(request):
    users=User.objects.filter(is_active=True)
    return render(request,'user/list.html',{'section':'people','users':users})

@login_required
def user_details(request,username):
    user=get_object_or_404(User,username=username,is_active=True)
    return render(request,'account/user/detail.html',{'section':'people','user':user})
    
