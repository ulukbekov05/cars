from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(90)], null=True, blank=True)
    phone_number =PhoneNumberField(null=True, blank=True)
    STATUS_CHOICES =(
        ('owner', 'owner'),
        ('client',  'client')
    )
    status = models.CharField(max_length=53, choices=STATUS_CHOICES)

class CarMake(models.Model):
    car_make_name = models.CharField(max_length=43, unique=True)
    car_make_picture = models.ImageField(upload_to='car_make_image/')

    def __str__(self):
        return self.car_make_name


class CarModel(models.Model):
    car_model_name=models.CharField(max_length=53, unique=True)
    make_car = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model_name


class Car(models.Model):
    car_make = models.CharField(max_length=35)
    category =models.ForeignKey(CarModel, on_delete=models.CASCADE)
    make_car = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()
    cash = models.BooleanField()
    COLOR_CHOICES = (
        ('black', 'black'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('white', 'white')
    )
    color = models.CharField(max_length=43, choices=COLOR_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=40, decimal_places=2)
    RULE_CHOICES =(
        ('right', 'right'),
        ('left', 'left')
    )
    rule = models.CharField(max_length=43, choices=RULE_CHOICES, verbose_name='руль')
    mileage = models.PositiveSmallIntegerField(verbose_name='пробег')
    FUEL_CHOICES =(
        ('БЕНЗИН', 'БЕНЗИН'),
        ('СОЛЯРКА', 'СОЛЯРКА'),
        ('ГАЗ', 'ГАЗ'),
        ('электро', 'электро')
    )

    fuel = models.CharField(max_length=53, choices= FUEL_CHOICES,   verbose_name='топливо')
    video_car = models.FileField(upload_to='video_cars/', null=True, blank=True)
    data  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.car_make},'

class Phone(models.Model):
    phone = PhoneNumberField()
    number_user =models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    number_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='number_user')




class ImageCar(models.Model):
    image_car = models.ImageField(upload_to='car_picture/')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='image_cars')


class Network(models.Model):
    network= models.CharField(max_length=43)
    network_link = models.URLField()
    title = models.CharField(max_length=53, null=True, blank=True)
    user =models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car_network = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='network_cars')


class CommitCar(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    text= models.TextField()
    answer = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class SpareParts(models.Model):
    spare_part_name = models.CharField(max_length=54)

    def __str__(self):
        return self.spare_part_name


class Category(models.Model):
    category = models.CharField(max_length=42)
    spare_part = models.ForeignKey(SpareParts, on_delete=models.CASCADE)
    def __str__(self):
        return self.category



class Spare(models.Model):
    spares_name =models.CharField(max_length=76, null=True, blank=True)
    spares = models.ForeignKey(SpareParts, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    users = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    spare_cars = models.ImageField(upload_to='spare_picture/')
    phone = PhoneNumberField(null=True, blank=True)




class Cart(models.Model):
    userPro = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)



