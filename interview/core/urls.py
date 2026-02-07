from django.urls import path

from interview.core.views import InventoryListAfterDateView, DeactivateOrderView, GetOrdersBetweenEmbargoDates

'''
Was surprised this file was missing from the core app, was it intentional to have me add it?
'''

urlpatterns = [
    path("inventory-after-date/", InventoryListAfterDateView.as_view()),
    path("deactivate-order/", DeactivateOrderView.as_view()),
    path("orders-between-embargo-dates/", GetOrdersBetweenEmbargoDates.as_view()),
]