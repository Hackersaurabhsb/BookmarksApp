from .models import images,upload_images
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
class image_create_form(forms.ModelForm):
    class Meta:
        model=images
        fields=['title','url','description']
        widgets={
            'url':forms.HiddenInput,
        }
    def clean_url(self):
        url=self.cleaned_data['url']
        valid_extension=['jpg','jpeg','png']
        extension=url.rsplit('.',1)[1].lower()
        print(extension)
        if extension not in valid_extension:
            raise forms.ValidationError("The given image format is not supported (supported formats are jpg,jpeg,png)")
        return url
    #now overriding the save method of model form in order to download the image from the given  url and save it to the database
    #instead of saving the url to the database
    def save(self,force_insert=False,force_update=False,commit=True):
        image=super().save(commit=False)
        image_url=self.cleaned_data['url']
        name=slugify(image.title)
        extension=image_url.rsplit('.',1)[1].lower()
        image_name=f'{name}.{extension}'
        #download image from given url
        response=requests.get(image_url)
        image.image.save(image_name,ContentFile(response.content),save=False)
        if commit:
            image.save()
        return image


#below form is for uploading images directly
# class upload_image_form(forms.ModelForm):
#     class Meta:
#         model=upload_images
