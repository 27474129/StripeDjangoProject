from .models import Item
from django.db.models import QuerySet


class ItemRepository:
    @staticmethod
    def get_item(item_id: int) -> Item or None:
        item = Item.objects.filter(pk=item_id)
        return item[0] if len(item) != 0 else None

    @staticmethod
    def get_all_items() -> QuerySet:
        return Item.objects.all()
