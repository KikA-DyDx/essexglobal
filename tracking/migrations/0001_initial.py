# Generated by Django 5.1.1 on 2025-05-16 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Receiver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Sender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Package",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("shipping_from", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("total_worth", models.DecimalField(decimal_places=2, max_digits=10)),
                ("clearance_fee", models.DecimalField(decimal_places=2, max_digits=10)),
                ("dispatch_date", models.DateField()),
                ("arrival_date", models.DateField()),
                ("tracking_number", models.CharField(max_length=50, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("in_transit", "In Transit"),
                            ("delivered", "Delivered"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=50,
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tracking.receiver",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tracking.sender",
                    ),
                ),
            ],
        ),
    ]
