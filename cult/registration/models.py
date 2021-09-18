from django.db import models

# Create your models here.
class registration(models.Model):
    user_name = models.CharField(max_length=45)
    ph_no = models.CharField(max_length=35)
    gmail = models.CharField(max_length=45)
    password = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)
    key = models.CharField(max_length=6, null=True)


    def __str__(self):
        return self.user_name+'-'+self.ph_no+'-'+self.gmail+'-'+self.password


