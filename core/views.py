import logging
import stripe
from payment import config
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.views import View
from django.views.generic import TemplateView
from .repository import ItemRepository


logger = logging.getLogger("debug")


class BaseAPIView(APIView):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error(e)
            return Response({"success": False, "message": e})


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error(e)
            return HttpResponse(e)


class ItemView(BaseView, TemplateView):
    template_name = "core/item.html"

    def get(self, request, item_id, *args, **kwargs):
        kwargs["item_id"] = item_id
        return super().get(request, item_id, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_data"] = ItemRepository.get_item(kwargs["item_id"])
        return context


class BuyView(BaseAPIView):
    def get(self, request, *args, **kwargs):
        stripe.api_key = config.STRIPE_SECRET_KEY
        return Response({"success": True})
