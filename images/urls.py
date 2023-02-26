from django.urls import path
from . import views
#create your urls here
app_name='images'
urlpatterns=[
    path('create/',views.process_image_create_form,name='create'),
    path('detail/<int:id>/<slug:slug>/',views.image_detail,name='detail'),
    path('like/',views.image_like,name='like'),
    path('',views.image_list,name='list')
]
