from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class ProductCrudAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Product.objects.using('inventory_db').all().values()
        return Response({
            'products': queryset
        })

    def post(self, request, *args, **kwargs):
        name = request.data['name']
        quantity = request.data['quantity']
        shipping_status = request.data['shipping_status']
        added_by = request.data['added_by']

        new_product = Product.objects.using('inventory_db').create(
            name=name,
            quantity=quantity,
            shipping_status=shipping_status,
            added_by=added_by,
        )
        new_product.save()

        return Response({
            'status': 'created',
        })
