from django.db import models
from datetime import datetime


class Customer(models.Model):

    name = models.CharField(max_length=64, default='')
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=64)
    town = models.CharField(max_length=120, default='')
    animal = models.CharField(max_length=64)
    quantity = models.CharField(max_length=10)
    time = models.CharField(max_length=80)
    date_order = models.DateTimeField(default=datetime.now ,blank=True)
    heard = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.id}"


class Discount(models.Model):

    cpn_id = models.ForeignKey(Customer,
                               on_delete=models.CASCADE,
                               related_name='coupons', null=True)
    coupon = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.coupon}"


class Butcher(models.Model):

    name = models.CharField(max_length=64)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=64)
    town = models.CharField(max_length=120, default='')
    # img = models.ImageField(upload_to='butcher')
    experience = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    price = models.CharField(max_length=64)
    heard = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.name}: ({self.city[0:10:2]}) {self.mobile}"


