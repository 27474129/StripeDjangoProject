from django.urls import path, include
from .views import ItemView, BuyView, payment


urlpatterns = [
    path("item/<int:item_id>", ItemView.as_view(), name="item"),
    path("buy/<int:item_id>", BuyView.as_view(), name="buy"),
    path("payment", payment, name="payment"),
]
