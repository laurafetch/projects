from django.test import TestCase
from django.urls import reverse
import pytest
from shopping_list.models import ShoppingList

# Create your tests here.

# Confirm that pytest command is working
def test_simple_pass():
    assert True

# Test access to homepage
def test_homepage_access():
          url = reverse('inventory_list')
          assert url == "/"

# Test endpoint
@pytest.mark.django_db
def test_tbd():
       pass