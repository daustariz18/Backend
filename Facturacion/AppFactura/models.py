from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    precio = models.FloatField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.name


class Clients(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self) -> str:
        return self.first_name


class Bills(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)


class Bill_Products(models.Model):
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
