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
# def index(request):
#     print("Test Inventory")
#     queryset = Inventory.objects.all()
#     return render(request, "shopping_list/index.html", {'foods': queryset})


# class index(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/index.html'

#     def get(self, request):
#         queryset = Inventory.objects.all()
#         return Response({'foods': queryset})

# #Shopping list
# class shopping_list(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/tutorial_list.html'

#     def get(self, request):
#         queryset = ShoppingList.objects.all()
#         return Response({'items': queryset})

#Get food inventory
# @api_view('GET')
# def inventory_list(request):
#     foods = Inventory.objects.all()
#     name = request.GET.get('food_id', None)
#     if name is not None:
#         foods = foods.filter(title__icontains=name)
#     inventory_serializer = InventorySerializer(foods, many=True)
#     return JsonResponse(inventory_serializer.data, safe=False)

# Get shopping list
# /
@api_view(['GET'])
def get_list(request):
    current_list = ShoppingList.objects.all()
    shopping_list_serializer = ShoppingListSerializer(current_list, many=True)
    return JsonResponse(shopping_list_serializer.data, safe=False)

# Add item to shopping list
# api/shopping_list/
@api_view(['POST'])
def add_item(request):
    item_data = JSONParser().parse(request)
    shopping_list_serializer = ShoppingListSerializer(data=item_data)
    if shopping_list_serializer.is_valid():
        shopping_list_serializer.save()
        return JsonResponse(shopping_list_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(shopping_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Edit/Remove item shopping list
# api/shopping_list/<int:pk>/
@api_view(['PATCH', 'DELETE'])
def edit_item(request, pk):
    try:
        item = ShoppingList.objects.get(pk=pk)
    except ShoppingList.DoesNotExist:
        return JsonResponse({'message': 'The item is not in the shopping list'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        item_data = JSONParser().parse(request)
        shopping_list_serializer = ShoppingListSerializer(item, data=item_data, partial=True)
        if shopping_list_serializer.is_valid():
            shopping_list_serializer.save()
            return JsonResponse(shopping_list_serializer.data)
        return JsonResponse(shopping_list_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        item.delete()
        return JsonResponse({'message': 'Item was removed successfully!'}, status=status.HTTP_204_NO_CONTENT)