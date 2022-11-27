import logging
import stripe
from payment import config
from rest_framework.views import APIView
from django.http import HttpResponseNotFound, HttpResponse
from rest_framework.response import Response
from django.views import View
from django.views.generic import TemplateView
from .repository import ItemRepository
from django.urls import reverse
from .services import PaymentService
from payment import settings


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
        item = ItemRepository.get_item(item_id)
        if item is None:
            return HttpResponseNotFound("Товар не найден")
        else:
            kwargs["item"] = item
        return super().get(request, item_id, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_data"] = kwargs["item"]
        return context


class BuyView(BaseAPIView):
    def get(self, request, item_id, *args, **kwargs):
        stripe.api_key = config.STRIPE_SECRET_KEY

        line_item = PaymentService.get_line_items(item_id)
        url = f"http://{settings.ALLOWED_HOSTS[0]}:8000{reverse('payment')}"
        session = stripe.checkout.Session.create(
            line_items=line_item,
            api_key=stripe.api_key,
            mode="payment",
            success_url=url,
            cancel_url=url,
        )
        return Response({"success": True, "response": {"session": session, "line_item": line_item}})


def payment(request):
    return HttpResponse("success")
