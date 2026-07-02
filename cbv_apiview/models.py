from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    desc = models.CharField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural = 'Maxsulotlar'
        verbose_name = 'Mahsulot'
        ordering = ['-id']
        db_table = 'products'
            
            
