from django.urls import path

from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path("my_order", MyOrderView.as_view(), name="my_order"),
    path("add_to_cart", CreateOrderProductView.as_view(), name="add_to_cart"),
]