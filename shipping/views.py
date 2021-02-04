from django.shortcuts import render
from rest_framework.views import APIView

from .models import Delivery


class ShippingCrudAPI(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Delivery.objects.using('shipping_db').all().values()
        return Response({
            'deliveries': queryset
        })

    def post(self, request, *args, **kwargs):
        product_id = request.data['product_id']
        shipping_status = request.data['shipping_status']

        new_deliver = Delivery.objects.using('inventory_db').create(
            product_id=product_id,
            shipping_status=shipping_status
        )
        new_deliver.save()

        return Response({
            'status': 'created',
            'data': new_deliver
        })
