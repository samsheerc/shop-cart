from django.shortcuts import render,redirect
from django.http import  JsonResponse
from shop.form import customerUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json



def home(request):
    products=product.objects.filter(treading=1)
    return render(request,"shop/index.html",{"products":products})

def favviewpage(request):
   if request.user.is_authenticated:
      fav = Favourite.objects.filter(user=request.user)
      return render(request,"shop/fav.html",{"fav":fav})
   else:
      return redirect("home")
   
def remove_fav(request,fid):
  item=Favourite.objects.filter(id=fid)
  print(item)
  item.delete()
  return redirect("/favviewpage")
 

def cart_page(request):
   if request.user.is_authenticated:
      cart=Cart.objects.filter(user=request.user)
      return render(request,"shop/cart.html",{"cart":cart})
   else:
      return redirect("home")
   

def remove_cart(request,cid):
   cartitem=Cart.objects.get(id=cid)
   cartitem.delete()
   return redirect("/cart")  

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)



 
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)



         
          

def loginout_page(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request,"Logged out successfully")
      return redirect("home")
    
   
   
def login_page(request):
  if request.user.is_authenticated:
    return redirect("home")
  else:
    if request.method=='POST': 
     name=request.POST.get('username')
     pwd=request.POST.get('password')
     user=authenticate(request,username=name,password=pwd)  
     if user is not None:
        login(request,user)
        messages.success(request,"Logged in Successfully")
        return redirect("home")
     else:
        messages.error(request,"invalid user name or password")
        return redirect("login")
          
    return render(request,"shop/login.html")         
             

def register(request):
    form=customerUserForm()
    if request.method=='POST':
       form=customerUserForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,"Registration sucess you can login now..!")
          return redirect("login")
    return render(request,"shop/register.html",{'form':form})


def collections(request):
    Category=category.objects.filter(status=0)
    return render(request,"shop/collection.html",{"category":Category})

def collectionview(request,name):
    if(category.objects.filter(name=name,status=0)):
        products=product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
    
    else:
        messages.warning(request,"NO Such Category found")
        return redirect('collection')

def product_detailview(request,cname,pname):
    if(category.objects.filter(name=cname,status=0)):
      if(product.objects.filter(name=pname,status=0)):
        products=product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_detail.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')
    
