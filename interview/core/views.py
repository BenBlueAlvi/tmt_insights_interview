
# Why include this if I'm supposed to write unit tests?
from django.shortcuts import render

from datetime import datetime

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from interview.core.serializers import InventoryListAfterDateViewSerializer, DeactivateOrderViewSerializer, \
    GetOrdersBetweenEmbargoDatesSerializer
from interview.inventory.models import Inventory
from interview.inventory.serializers import InventorySerializer
from interview.order.models import Order
from interview.order.serializers import OrderSerializer


# Create your views here.

class InventoryListAfterDateView(APIView):
    serializer_class = InventoryListAfterDateViewSerializer
    inventory_serializer_class = InventorySerializer

    def post(self, request: Request, *args, **kwargs) -> Response:

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()

        date_after: datetime = serializer.get_date()
        inventory_after_date = Inventory.objects.filter(
            created_at__gte=date_after
        )

        return Response(self.inventory_serializer_class(inventory_after_date, many=True).data, status=200)


class DeactivateOrderView(APIView):
    serializer_class = DeactivateOrderViewSerializer
    order_serializer_class = OrderSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()

        order = Order.objects.filter(id=serializer.get_id()).first()
        if not order:
            return Response(serializer.errors, status=400)

        order.is_active = False
        order.save()

        return Response(self.order_serializer_class(order).data, status=200)


class GetOrdersBetweenEmbargoDates(APIView):
    serializer_class = GetOrdersBetweenEmbargoDatesSerializer
    order_serializer_class = OrderSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        serializer.save()

        '''
        Was a little confused on what was being asked here, 
        'orders that are between a particular start and embargo date.' isn't clear on what
        an order is or is not. Does it mean that both the start and the embargo date are within
        the specified range? or is it two separate ranges for both dates? or is that they were created
        between the two dates?
        '''
        orders = Order.objects.filter(
            start_date__gte=serializer.get_start_date(),
            embargo_date__lte=serializer.get_embargo_date()
        )
        return Response(self.order_serializer_class(orders, many=True).data, status=200)

