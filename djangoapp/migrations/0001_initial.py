# Generated by Django 5.0.2 on 2024-02-13 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("perishable", "Perishable"),
                            ("non-perishable", "Non-Perishable"),
                        ],
                        max_length=50,
                    ),
                ),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("zone", models.CharField(max_length=100)),
                ("base_distance_in_km", models.IntegerField(default=5)),
                ("km_price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("fix_price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="djangoapp.item"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djangoapp.organization",
                    ),
                ),
            ],
        ),
    ]
