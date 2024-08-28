from django.shortcuts import render
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from shopping_list.models import Food, ShoppingList, Inventory
from shopping_list.serializers import FoodSerializer, ShoppingListSerializer, InventorySerializer
from rest_framework.decorators import api_view

#Inventory list
def index(request):
    print("Test Inventory")
    queryset = Inventory.objects.all()
    return render(request, "shopping_list/index.html", {'foods': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shopping_list/index.html'

    def get(self, request):
        queryset = Inventory.objects.all()
        return Response({'foods': queryset})

#Shopping list
class shopping_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'shopping_list/tutorial_list.html'

    def get(self, request):
        queryset = ShoppingList.objects.all()
        return Response({'items': queryset})


@api_view('GET')
def inventory_list(request):
    foods = Inventory.objects.all()
    name = request.GET.get('food_id', None)
    if name is not None:
        foods = foods.filter(title__icontains=name)
    inventory_serializer = InventorySerializer(foods, many=True)
    return JsonResponse(inventory_serializer.data, safe=False)