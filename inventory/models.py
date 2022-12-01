from django.db import models

class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    name = models.CharField("Fullname", max_length=50)


    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    the_name = models.CharField("Product Name", max_length=100, help_text="This is the help text")
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ["age"]
    
    def __str__(self):
        return self.the_name

class Stock(models.Model):
    units = models.BigIntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return "Stocks"