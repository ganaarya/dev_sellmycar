from django.db import models

# Create your models here.

class Car(models.Model):

    #CHOICES:
    BRAND = (
        ('TOY','Toyota'),
        ('MZD','Mazda'),
        ('LXS','Lexus'),
        ('BMW','BMW'),
        ('PRS','Porsche'),
        ('MCB','Mercedes-Benz'),
        ('HND','Honda'),
        ('NSN','Nissan'),
        ('MBS','Mitsubishi'),
        ('CVL','Chevrolet'),
        ('FRD','Ford'),
        ('HYD','Hyundai')
    )

    TRANSMISSION = (
        ('AT','Automatic'),
        ('MT','Manual'),
    )

    owners_name = models.CharField(max_length=264)
    brand = models.CharField(max_length=3, choices=BRAND)
    type = models.CharField(max_length=264)
    car_model = models.CharField(max_length=264)
    year = models.CharField(max_length=264)
    transmission = models.CharField(max_length=2, choices=TRANSMISSION)
    owners_email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=254)

    def __str__(self):
        return "%s %s %s"%(self.brand,self.car_model,self.year)
