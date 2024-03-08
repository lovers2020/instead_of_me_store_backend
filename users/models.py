from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = "남성"
        FEMALE = "여성"

    name = models.CharField(max_length=20, default="", verbose_name="이름")
    gender = models.CharField(
        max_length=10, choices=GenderChoices.choices, verbose_name="성별"
    )
    address = models.CharField(max_length=200, verbose_name="주소")
    email = models.EmailField(verbose_name="이메일")
    phone_number = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed.",
            )
        ],
        default="",
    )

    birth = models.CharField(
        verbose_name="생년월일",
        default="",
        max_length=8,
        validators=[
            RegexValidator(
                regex=r"^(19[0-9][0-9]|20\d{2})(0[0-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])$",
                message="생년월일은 8자리로 표현해야합니다.",
            )
        ],
    )
    is_host = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
