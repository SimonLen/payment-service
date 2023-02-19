from django.db import models


class Item(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_display_price(self):
        return '{0:.2f}'.format(self.price / 100)
