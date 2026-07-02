from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from cbv_apiview.models import Product
from cbv_apiview.serializer import ProductSerializer
from rest_framework.generics import GenericAPIView

def response_model(msg, status_code, data = None):
    return Response({
        'msg': msg,
        'status': status_code,
        'data': data
    })

class ListCreateApiview(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset, many = True)
        return response_model('Product list', status.HTTP_200_OK, serializer.data)
    
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        
        return response_model('Product create', status.HTTP_201_CREATED, serializer.data)


class UpdateDeleteDetial(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    def get_object(self, request, pk):
        product = Product.objects.filter(pk = pk).first()
        if not product:
            raise ValidationError({
                'error':'Product not found', 
                'status':status.HTTP_204_NO_CONTENT
            })
        return product
    def get(self, pk):
        product = self.get_object(pk)
        serializer = self.get_serializer(product)
        
        
        return response_model('Product updete', status.HTTP_200_OK, serializer.data)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = self.get_serializer(instance = product, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
                
        return response_model('Product update', status.HTTP_200_OK, serializer.data)
    def putch(self, request, pk):
            product = self.get_object(pk)
            serializer = self.get_serializer(instance = product, data = request.data, partial = True)
            serializer.is_valid(raise_exception = True)
            serializer.save()
            return response_model('Product update', status.HTTP_200_OK, serializer.data)
    def delete(self, pk):
            product = self.get_object(pk)
            product.delete()
            return response_model('Product update', status.HTTP_204_NO_CONTENT)