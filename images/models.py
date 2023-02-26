from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
#foreign key is a one to many relation
#############################################################################################################
class images(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
#     Next, we will add another field to the Image model to store the users who like an image. We will need 
# a many-to-many relationship in this case because a user might like multiple images and each image 
# can be liked by multiple users.
    users_like=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='images_liked',blank=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,blank=True)
    url=models.URLField(max_length=2000)
    image=models.ImageField(upload_to='images/%y/%m/%d/')
    description=models.TextField(blank=True)
    created=models.DateField(auto_now_add=True)
    class Meta:
        indexes=[
            models.Index(fields=['-created']),
        ]
        ordering=['-created']

    def __str__(self):
        return self.title
#     We will override the save() method of the Image model to automatically generate the slug field based 
# on the value of the title field. Import the slugify() function and add a save() method to the Image
# model, as follows. New lines are highlighted in bold
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('images:detail',args=[self.id,self.slug])
#     Remember that the common pattern for providing canonical URLs for objects is to define a get_
#     absolute_url() method in the model.

###############################################################################################################
# user: This indicates the User object that bookmarked this image. This is a foreign key field 
# because it specifies a one-to-many relationship: a user can post multiple images, but each 
# image is posted by a single user. We have used CASCADE for the on_delete parameter so that 
# related images are deleted when a user is deleted.
# • title: A title for the image.
# • slug: A short label that contains only letters, numbers, underscores, or hyphens to be used 
# for building beautiful SEO-friendly URLs.
# • url: The original URL for this image. We use max_length to define a maximum length of 2000
# characters.
# • image: The image file.
# • description: An optional description for the image.
# • created: The date and time that indicate when the object was created in the database. We 
# have added auto_now_add to automatically set the current datetime when the object is created.

class upload_images(models.Model):
    images=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='uploaded_image',on_delete=models.CASCADE)
    caption=models.TextField(blank=True)
    upload_time=models.DateTimeField(auto_now_add=True)
    