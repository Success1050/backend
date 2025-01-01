from django.db import models

# Create your models here.

class Comment(models.Model):
    name= models.CharField(max_length=62)
    email= models.EmailField()
    # image= models.ImageField(default= 'default.png', blank= True)
    message= models.TextField()
    created= models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering= ['-created']

    def __str__(self):
        return self.name