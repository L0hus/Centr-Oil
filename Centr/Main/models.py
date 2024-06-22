from django.db import models

class Product(models.Model):
    type = models.CharField(max_length=50,)
    typeForName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gost = models.CharField(max_length=200)
    base = models.TextField(max_length=2000)
    pack = models.TextField(max_length=200000)
    area = models.TextField(max_length=200000)
    feature = models.TextField(max_length=200000)
    characteristic = models.TextField(max_length=200000)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    ip_address = models.GenericIPAddressField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
