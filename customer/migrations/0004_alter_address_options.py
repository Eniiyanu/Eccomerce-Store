# Generated by Django 4.1.1 on 2022-09-13 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0003_alter_address_country"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={
                "verbose_name": " Delivery Address",
                "verbose_name_plural": " Delivery Addresses",
            },
        ),
    ]