
from django.db import models
from django.contrib.auth.models import User
import datetime
import os
from .models import *


def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('upload/',new_filename)

class category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=True)
    image=models.ImageField(upload_to=getfilename,null=True,blank=False)
    description=models.TextField(max_length=500,null=True,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name
    

class product(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=True)
    vendor=models.CharField(max_length=150,null=False,blank=True)
    product_image=models.ImageField(upload_to=getfilename,null=True,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField(max_length=500,null=True,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    treading=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name    

class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
 
  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price    


class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
 