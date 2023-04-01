# Generated by Django 4.1.1 on 2022-09-22 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0008_remove_address_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="customer.customer",
            ),
        ),
    ]