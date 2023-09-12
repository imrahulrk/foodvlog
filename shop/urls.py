from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),  
    path('login', views.login_view),
    path('logout', views.logout_view, name='logout'),
    # Add more URL patterns as needed




]