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
    

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('ice-cream', 'Ice Cream'),
    ('softy', 'Softy'),
    ('family-pack', 'Family Pack'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name