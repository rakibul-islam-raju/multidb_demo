from django.db import models


class Product(models.Model):
    SHIPPING_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('out_for_deliver', 'Out for Deliver'),
        ('delivered', 'Delivered'),
    )
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    shipping_status = models.CharField(max_length=20, default='pending', choices=SHIPPING_STATUS_CHOICES)
    added_by = models.IntegerField()

    def __str__(self):
        return self.name
