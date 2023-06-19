from django.urls import path
from webApp import views


urlpatterns = [
     path('homepage/',views.homepage,name="homepage"),

     path('contactpage/',views.contactpage,name="contactpage"),
     path('productpage/<cateName>',views.productpage,name="productpage"),
     path('singleProductpage/<int:dataid>',views.singleProductpage,name="singleProductpage"),
     path('loginpage/',views.loginpage,name="loginpage"),
     path('userRegData/',views.userRegData,name="userRegData"),
     path('userLogin/',views.userLogin,name="userLogin"),
     path('userLogout/',views.userLogout,name="userLogout"),
     path('contactData/',views.contactData,name="contactData"),
     path('cartpage/',views.cartpage,name="cartpage"),
     path('cartData/',views.cartData,name="cartData"),
     path('deletecartData/<int:dataid>/',views.deletecartData,name="deletecartData"),
     path('checkout/',views.checkout,name="checkout"),
     path('checkoutform/',views.checkoutform,name="checkoutform"),
     
     
]