from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    product_image = models.TextField()
    product_price = models.IntegerField()


    def __str__(self) -> str:    
        return self.product_name                      

class Order(BaseModel):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="orders" )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, null=True , blank=True)
    order_id = models.CharField(max_length=500, null=True , blank=True)
    instamojo_response = models.TextField(null=True , blank=True)        

