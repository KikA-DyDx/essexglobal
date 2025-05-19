from django.db import models
import uuid

# Currency choices
CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('ZAR', 'Rand'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
]

# Sender model


class Sender(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

# Receiver model


class Receiver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

# Package model


class Package(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    shipping_from = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    description = models.TextField()

    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='USD'
    )

    clearance_fee = models.DecimalField(max_digits=10, decimal_places=2)
    clearance_fee_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='USD'
    )

    dispatch_date = models.DateField()
    arrival_date = models.DateField()

    tracking_number = models.CharField(max_length=50, unique=True, blank=True)

    status = models.CharField(
        max_length=50,
        choices=[
            ('pending', 'Pending'),
            ('awaiting_clearance', 'Awaiting Clearance'),
            ('in_transit', 'In Transit'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Tracking: {self.tracking_number}"

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = str(
                uuid.uuid4()).replace('-', '').upper()[:12]
        super().save(*args, **kwargs)
