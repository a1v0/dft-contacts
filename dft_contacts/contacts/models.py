from django.db import models
from enum import Enum


class TypeEnum(Enum):
    FAMILY = 1, "Family"
    FRIENDS = 2, "Friends"
    WORK = 3, "Work"
    TRADE = 4, "Trade"
    OTHER = 5, "Other"


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    type = models.IntegerField(
        choices=[(type.value[0], type.value[1]) for type in TypeEnum]
    )
