from django.db import models

# Create your models here.
class home(models.Model):
    id_no = models.CharField(max_length=10)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.id_no+'-'+self.location