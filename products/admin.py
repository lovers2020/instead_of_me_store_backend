from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "details",
        "size",
        "stock",
        "gender",
        # "main_image",
        # "detail_image1",
        # "detail_image2",
        # "detail_image3",
        # "detail_image4",
        # "detail_image5",
        # "detail_image6",
    )
