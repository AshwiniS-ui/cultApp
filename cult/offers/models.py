from django.db import models

# Create your models here.
class offers(models.Model):
    offer_name = models.CharField(max_length=50)
    offer_description = models.CharField(max_length=50)
    offer_cost = models.CharField(max_length=150)
    offer_duration = models.CharField(max_length=50)
    offer_discount = models.CharField(max_length=50)
    bank_offers = models.CharField(max_length=250)

    def __str__(self):
        return self.offer_name+'-'+self.offer_description+'-'+self.offer_cost+'-'+self.offer_duration+'-'+self.offer_discount+'-'+self.bank_offers
