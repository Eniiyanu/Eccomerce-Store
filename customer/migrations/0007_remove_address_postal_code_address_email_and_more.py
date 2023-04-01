# Generated by Django 4.1.1 on 2022-09-22 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0006_alter_address_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="postal_code",
        ),
        migrations.AddField(
            model_name="address",
            name="email",
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="first_name",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="last_name",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="address",
            name="phone",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
