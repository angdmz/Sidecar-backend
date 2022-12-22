import uuid

from django.db import models

# Create your models here.
from django.db.models import CharField


class Investor(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4)
    full_legal_name = CharField(max_length=80)


class Asset(models.Model):
    PUBLIC_STOCK = "PUBLIC_STOCK"
    TYPE = [
        (PUBLIC_STOCK, 'Public stock'),
    ]
    type = models.CharField(
        max_length=50,
        choices=TYPE,
        default=PUBLIC_STOCK,
    )
    name = models.CharField(max_length=50, null=True)


class Investment(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name="investments")
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name="investments")
    invested_since = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    shares = models.BigIntegerField(null=False)
    purchase_price = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    current_price = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("asset", "investor", "created_at")
