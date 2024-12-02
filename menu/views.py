from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .serializers import ItemSerializer
from .models import Item

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
'''def item_list(request):
    items = Item.objects.all()
    # We will serialize items which is a query object into a python list
    # Serialization is the fact of changing data types into other data types
    item_list = []
    for item in items:
        item_list.append({
            "name": item.name,
            "price": item.price,
            "description": item.description})
    return JsonResponse({"menu_items": item_list}, safe=False)'''

# The code up is without djangoRestFramework - 

@api_view(['Get', 'POST'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
# The code bellow is using djangoRestFramework

def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
