from django.db import models
import datetime

# Create your models here.
class Food(models.Model):
    name = models.TextField(unique=True)
    auto_buy = models.BooleanField(default=False)

    class Meta:
        db_table = "foods"

    # def __init__(self, name: str, auto_buy: str):
    #     self.name = name
    #     self.auto_buy = auto_buy

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "auto_buy": self.auto_buy
    #     }

class ShoppingList(models.Model):
    food_id = models.ForeignKey("Food", on_delete=models.CASCADE, unique=True)
    num_units = models.IntegerField(default=1)
    date_added = models.DateField()

    class Meta:
        db_table = "shopping_list"

    # def __init__(self, food_id: int, num_units: int, date_added: datetime):
    #     self.food_id = food_id
    #     self.num_units = num_units
    #     self.date_added = date_added

    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'food_id': self.food_id,
    #         'date_added': self.date_added.isoformat(),
    #         'num_units': self.num_units
    #     }

class Inventory(models.Model):
    food_id = models.ForeignKey("Food", on_delete=models.CASCADE, unique=True)
    in_stock = models.BooleanField()
    expiration_date = models.DateField()

    class Meta:
        db_table = "inventory"