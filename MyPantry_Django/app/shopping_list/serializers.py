from rest_framework import serializers
from shopping_list.models import Food, ShoppingList, Inventory


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'auto_buy')

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('food_id', 'num_units', 'date_added')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('food_id', 'in_stock', 'expiration_date')        