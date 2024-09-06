from django.test import TestCase
from django.urls import reverse
import pytest
from shopping_list.models import ShoppingList

# Create your tests here.

# Confirm that pytest command is working
def test_simple_pass():
    assert True


# Test adding item
@pytest.mark.django_db
def test_create_item():
    request = ShoppingList.objects.create(
	food_id = 2,
	num_units = 1,
	date_added = "2024-08-20"
)
    assert request.food_id == "2"
    