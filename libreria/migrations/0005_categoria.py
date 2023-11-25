# Generated by Django 4.2.7 on 2023-11-25 04:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("libreria", "0004_reserva"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
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
                ("nombre", models.CharField(max_length=200)),
            ],
        ),
    ]
