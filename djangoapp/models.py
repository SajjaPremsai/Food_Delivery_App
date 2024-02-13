from django.db import models

# Create your models here.


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Item(models.Model):
    PERISHABLE = 'perishable'
    NON_PERISHABLE = 'non-perishable'

    ITEM_TYPES = [
        (PERISHABLE, 'Perishable'),
        (NON_PERISHABLE, 'Non-Perishable'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=ITEM_TYPES)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Pricing(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.IntegerField(default=5)
    km_price = models.DecimalField(max_digits=6, decimal_places=2)
    fix_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.item.type == 'perishable':
            self.km_price = 1.5
        else:
            self.km_price = 1.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pricing for {self.organization.name} - {self.item.description}"