from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
#the current model is for views login view
# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #The one-to-one field user will be used to associate profiles with users. With on_delete=models.CASCADE, 
    #we force the deletion of the related Profile object when a User object gets deleted.
    date_of_birth=models.DateTimeField(blank=True,null=True)
    photo=models.ImageField(upload_to='users/%y/%m/%d/',blank=True,null=True)
    def __str__(self):
        return f'Profile of {self.user.username}'

#In order to keep your code generic, use the get_user_model() method to retrieve the user 
#model and the AUTH_USER_MODEL setting to refer to it when defining a model’s relationship 
#with the user model, instead of referring to the auth user model directly.


#here is the intermediary model to build the follow system
class contact(models.Model):
    user_from=models.ForeignKey('auth.User',related_name="rel_from_set",on_delete=models.CASCADE)
    user_to=models.ForeignKey('auth.User',related_name="rel_to_set",on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes=[
            models.Index(fields=['-created'])
        ]
        ordering=['-created']
    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


# When you need additional fields in a many-to-many relationship, create a custom model 
# with a ForeignKey for each side of the relationship. Add a ManyToManyField in one of 
# the related models and indicate to Django that your intermediary model should be used 
# by including it in the through parameter.

# If the User model was part of your application, you could add the previous field to the model. However, 
# you can’t alter the User class directly because it belongs to the django.contrib.auth application. Let’s 
# take a slightly different approach by adding this field dynamically to the User model.
#here we are adding a manytomany field to every users dynamically

user_model=get_user_model()
user_model.add_to_class('following',models.ManyToManyField('self',through=contact,related_name='followers',symmetrical=False))
# Be aware that using add_to_class() is not the recommended way of adding fields to models. However, you take advantage of using it in this case to avoid creating a custom user model, keeping all the 
# advantages of Django’s built-in User model.
# Note that the relationship includes symmetrical=False. When you define a ManyToManyField in the 
# model creating a relationship with itself, Django forces the relationship to be symmetrical. In this 
# case, you are setting symmetrical=False to define a non-symmetrical relationship (if I follow you, it 
# doesn’t mean that you automatically follow me).
# When you use an intermediary model for many-to-many relationships, some of the related manager’s methods are disabled, such as add(), create(), or remove(). You need to 
# create or delete instances of the intermediary model instead.
