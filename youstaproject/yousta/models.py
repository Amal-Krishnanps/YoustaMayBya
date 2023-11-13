from django.db import models
from django.contrib.auth.models import AbstractUser



# customizing user model, when u customz. then point it in settings & register in admin.py
class User(AbstractUser):
    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=200)

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Cloths(models.Model):
    name=models.CharField(max_length=200)
    options=(
        ("linen","linen"),
        ("cotton","cotton"),
        ("satin","satin"),
        ("nylon","nylon"),
        ("polyster","polyster"),
        ("silk","silk")
    )
    material=models.CharField(max_length=200,choices=options,default="cotton")
    image=models.ImageField(upload_to="images")
    brand=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class ClothVarients(models.Model):
    price=models.PositiveIntegerField()
    color=models.CharField(max_length=100)
    options=(
        ("S","S"),
        ("M","M"),
        ("L","L"),
        ("XL","XL"),
        ("XXL","XXL")
    )
    size=models.CharField(max_length=200,choices=options,default="M")
    cloth=models.ForeignKey(Cloths,on_delete=models.CASCADE)

class Offers(models.Model):
    ClothVarient=models.ForeignKey(ClothVarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()


class Carts(models.Model):
    ClothVarient=models.ForeignKey(ClothVarients,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
        )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ClothVarient=models.ForeignKey(ClothVarients,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
        )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    ordered_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator
class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ClothVarient=models.ForeignKey(ClothVarients,on_delete=models.CASCADE)
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)
    
