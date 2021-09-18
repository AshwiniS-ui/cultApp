from django.db import models

# Create your models here.
class login(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name+'-'+self.password
