from django.contrib import admin
from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product",
        "quantity",
        "total_price",
    )
