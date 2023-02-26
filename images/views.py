from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import image_create_form
from .models import images
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# We will use JavaScript requests to build 
# an infinite scroll functionality. Infinite scroll is achieved by loading the next results automatically 
# when the user scrolls to the bottom of the page.
# Create your views here.
@login_required()
def process_image_create_form(request):
    if request.method=='POST':
        form_instance=image_create_form(data=request.POST)
        if form_instance.is_valid():
            cd=form_instance.cleaned_data
            new_image=form_instance.save(commit=False)
            #assign a user to the image object
            new_image.user=request.user
            new_image.save()
            messages.success(request,"Image added successfully")
            return redirect(new_image.get_absolute_url())
    else:
        form_instance=image_create_form(data=request.GET)
        return render(request,'images/image_upload.html',{'section':'images','form':form_instance})


def image_detail(request,id,slug):
    Image=get_object_or_404(images,id=id,slug=slug)
    return render(request,'images/detail.html',{'section':'images','image':Image})

@login_required
@require_POST
def image_like(request):
    image_id=request.POST.get('id')
    action=request.POST.get('action')
    print(image_id)
    print(action)
    if image_id and action:
        print("inside if block")
        try:
            print("inside try block")
            image=images.objects.get(id=image_id)
            print(image)
            if action=='like':
                image.users_like.add(request.user)
                print("user added")
            else:
                image.users_like.remove(request.user)
                print("user removed")
            return JsonResponse({'status':'ok'})
        except images.DoesNotExist:
            pass
    return JsonResponse({'status':'error'})

@login_required
def image_list(request):
    Image=images.objects.all()
    paginator=Paginator(Image,8)
    page=request.GET.get('page')
    images_only=request.GET.get('images_only')
    try:
        Image=paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        Image=paginator.page(1)
    except EmptyPage:
        if images_only:
            #if ajax request and page are out of range then return empty page
            return HttpResponse('')
        #if page out of range return last page
        Image=paginator.page(paginator.num_pages)
    if images_only:
        return render(request,"images/list_images.html",{'section':'images','images':Image})
    return render(request,"images/list.html",{'section':'images','images':Image})
    