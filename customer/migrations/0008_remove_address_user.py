# Generated by Django 4.1.1 on 2022-09-22 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0007_remove_address_postal_code_address_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="user",
        ),
    ]
