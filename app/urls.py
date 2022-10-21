from django.urls import path
from . import views 


urlpatterns = [
    # path('',views.message),
    path('about/', views.about),
    path('contact/', views.contact),
    path('', views.home),
    path('form/', views.form , name='form'),
]
