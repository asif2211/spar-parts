from django.db import models


class Item(models.Model):
    item = models.CharField(max_length=200)

    def __str__(self):
        return self.item


class Product(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    total_qty = models.IntegerField(default=0)
    unit_cost = models.IntegerField(default=0)
    image = models.CharField(default=0, max_length=300)
    date = models.DateField(default=0)

    def __str__(self):
        return self.item_name.item


class Sale(models.Model):
    item_name = models.ForeignKey(Item, on_delete=models.CASCADE)
    sold_qty = models.IntegerField(default=0)
    sale_unit = models.IntegerField(default=0)
    date = models.DateField(default=0)

    def __str__(self):
        return self.item_name.item
