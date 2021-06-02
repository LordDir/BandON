from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# blank можно оставить пустым null ограничение на пустое поле

class Musician(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length=100, null = True)
    #phone = models.CharField()
    email = models.EmailField(null = True)
    description = models.CharField(max_length = 150, null = True)
    like = models.IntegerField(default = 0)
    #profile_pic = modles.ImageField(null = True, blank = True)
    #liked = models.BooleanField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name 

    #возможно позднее понадобится
    #class Meta:
    #   ordering = ['liked']    
