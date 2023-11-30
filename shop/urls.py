from django.urls import path
from .import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.loginout_page,name='logout'),
    path('register/',views.register,name='register'),
    path('cart/',views.cart_page,name='cart'),
    path('fav',views.fav_page,name='fav'),
    path('favviewpage',views.favviewpage,name='favviewpage'),
    path('remove_fav/<int:fid>',views.remove_fav,name='remove_fav'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('collection/',views.collections,name='collection'),
    path('collection/<str:name>',views.collectionview,name='collection'),
    path('collections/<str:cname>/<str:pname>',views.product_detailview,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
]