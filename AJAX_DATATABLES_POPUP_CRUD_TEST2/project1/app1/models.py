from django.db import models

# Create your models here.
class Post(models.Model):
    
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    remark = models.TextField()
 
    # with their title name
    def __str__(self):
        return self.title