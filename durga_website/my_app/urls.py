from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('shuga_magazine/', views.shuga_magazine, name='shuga_magazine'),
    path('ary_world/', views.ary_world, name='ary_world'),
    path('mission/', views.mission, name='mission'),
    path('pricing/', views.pricing, name='products'),
   
]