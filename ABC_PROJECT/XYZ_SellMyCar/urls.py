from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from XYZ_SellMyCar import views

#TEMPLATE TAGGING
app_name = 'SellMyCar'

urlpatterns = [
    url('^home/$', views.home_page, name="home_page"),
    url('^car-register/$', views.car_register_page, name="car_register_page"),
    url('^gallery/$', views.gallery_page, name="gallery_page"),
    url('^about/$', views.about_page, name="about_page"),
]
