from django.urls import path
from .views import ListCreateApiview, UpdateDeleteDetial

urlpatterns = [
    path('create/', ListCreateApiview.as_view()),
    path('update/', UpdateDeleteDetial.as_view()),
    
]