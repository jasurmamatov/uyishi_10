from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Product
from .serializer import ProductSerializer
from rest_framework.views import APIView
# Create your views her



class CreateProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        
        return Response({
            'msg':'Created Product',
            'status': status.HTTP_201_CREATED,
            'product':serializer.data
        }
        
)
class ListProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response({
            'msg': 'Product List',
            'status': status.HTTP_200_OK,
            'product': serializer.data
        })



class UpdateProductView(APIView):
    def get_object(self, pk):
        product = Product.objects.filter(pk = pk).first()
        if not product:
            raise ValidationError(
                {
                    'msg': 'Product not found',
                    'status': status.HTTP_204_NO_CONTENT,
                }
            )
    def get(self, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        
        return Response({
            'msg': 'Product List',
            'status': status.HTTP_200_OK,
            'product': serializer.data
        })
    def put(self,request, pk):
            product = self.get_object(pk)
            serializer = ProductSerializer(isinstance = product  , data = request.data)
            
            return Response({
                'msg': 'Product Update',
                'status': status.HTTP_200_OK,
                'product': serializer.data
            })
    def putch(self,request, pk):
                product = self.get_object(pk)
                serializer = ProductSerializer(isinstance = product  , data = request.data, partial = True)
                
                return Response({
                    'msg': 'Product Update',
                    'status': status.HTTP_200_OK,
                    'product': serializer.data
                })
    def delete(self, pk):
                product = self.get_object(pk)  
                product.delete()              
                return Response({
                    'msg': 'Product Update',
                    'status': status.HTTP_204_NO_CONTENT,
                })