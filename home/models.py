from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    #if description added the it will be a textField
    date=models.DateField()

    #A function so that when a new entry is added in data base it will have a name instead 
    #of having name= contact object
    def __str__(self):
        return self.name    #if you want to see your entrie as name ,you can also see them as email and phone etc
    

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', default='products/default.jpeg')

    category = models.CharField(max_length=100)  # e.g., 'ice-cream', 'softy', 'family-pack'

    def __str__(self):
        return self.name

