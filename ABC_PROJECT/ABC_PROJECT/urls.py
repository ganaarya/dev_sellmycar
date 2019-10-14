"""ABC_PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include

from XYZ_SellMyCar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.home_page,name="home_page"),
    url('^XYZ_SellMyCar/', include('XYZ_SellMyCar.urls')),
    # url('^home/$', views.home_page, name="home_page"),
    # url('^car-register/$', views.car_register_page, name="car_register_pages"),
    # url('^gallery/$', views.gallery_page, name="gallery_page"),
    # url('^about/$', views.about_page, name="about_page"),

]
