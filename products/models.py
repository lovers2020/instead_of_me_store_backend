from django.db import models


class Product(models.Model):

    class GenderChoices(models.TextChoices):
        MEN = "남성"
        WOMEN = "여성"

    class SizeChoices(models.TextChoices):
        XS = ("xs", "XS")
        S = ("s", "S")
        M = ("m", "M")
        L = ("l", "L")
        XL = ("xl", "XL")

    name = models.CharField(max_length=50, verbose_name="상품명")
    price = models.PositiveIntegerField(verbose_name="가격")
    details = models.TextField(max_length=300, verbose_name="상품설명")
    stock = models.PositiveIntegerField(verbose_name="재고")
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        verbose_name="제품 성별",
        default="",
    )
    size = models.CharField(
        max_length=5,
        choices=SizeChoices.choices,
        verbose_name="사이즈",
        default="",
    )
    main_image = models.URLField(verbose_name="메인 이미지", default="")
    detail_image1 = models.URLField(verbose_name="상세이미지 1", default="", blank=True)
    detail_image2 = models.URLField(verbose_name="상세이미지 2", default="", blank=True)
    detail_image3 = models.URLField(verbose_name="상세이미지 3", default="", blank=True)
    detail_image4 = models.URLField(verbose_name="상세이미지 4", default="", blank=True)
    detail_image5 = models.URLField(verbose_name="상세이미지 5", default="", blank=True)
    detail_image6 = models.URLField(verbose_name="상세이미지 6", default="", blank=True)

    size_chart = models.URLField(verbose_name="사이즈 차트", default="", blank=True)
    materials = models.URLField(verbose_name="소재", default="", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shop_products"
        verbose_name = "상품"
        verbose_name_plural = "상품"
