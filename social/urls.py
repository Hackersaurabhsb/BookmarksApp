"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('social-auth',include('social_django.urls',namespace='social')),
    path('images/',include('images.urls',namespace='images')),
]
# Several social services will not allow redirecting users to 127.0.0.1 or localhost after 
# successful authentication; they expect a domain name for the URL redirect. First, we need to use a 
# domain name to make social authentication work.we done this in the windows host file
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#The static() helper function is suitable for development but not for production use. Django is very inefficient
#  at serving static files. Never serve your static files with Django in a production environment.