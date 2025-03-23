from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256,blank=False,null=False)
    description=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256,blank=False,null=False)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to="products",blank=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")

    def __str__(self):
        return self.name

    