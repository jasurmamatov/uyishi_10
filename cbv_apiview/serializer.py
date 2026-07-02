from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Ism kamida 3 ta harfdan iborat bo'lishi kerak."
            )
        return value   