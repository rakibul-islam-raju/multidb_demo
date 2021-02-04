from django.db import models


class Delivery(models.Model):
    SHIPPING_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('out_for_deliver', 'Out for Deliver'),
        ('delivered', 'Delivered'),
    )
    product_id = models.IntegerField()
    shipping_status = models.CharField(max_length=20, default='pending', choices=SHIPPING_STATUS_CHOICES)

    def __str__(self):
        return (f'{self.product_id} --> {self.shipping_status}')
    
