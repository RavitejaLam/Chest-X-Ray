from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Profile(models.Model):
#     user = models.OneToOneField(User,unique=True, null=False, db_index=True,on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)

class Testing(models.Model):
    image = models.ImageField(upload_to='chestxray_image/', blank=True)
    side = models.CharField(max_length=8)
    gender = models.CharField(max_length=8)
    submitted_on = models.DateField(("Date"),blank=True)
    description = models.TextField(max_length=2048,blank=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.first_name