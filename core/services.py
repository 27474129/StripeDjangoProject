from .repository import ItemRepository


class PaymentService:
    @staticmethod
    def get_line_items(item_id: int) -> list:
        item = ItemRepository.get_item(item_id=item_id)
        line_item = [{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": item.name,
                    "description": item.description
                },
                "unit_amount": int(item.price),
            },
            "quantity": 1
        }]
        return line_item
