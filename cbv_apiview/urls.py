from django.urls import path
from .views import CreateProductView, ListProductView

urlpatterns = [
    path('create/', CreateProductView.as_view()),
    path('list/', ListProductView.as_view()),
    
]