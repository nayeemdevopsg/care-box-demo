# Generated by Django 3.2.2 on 2021-05-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_banner_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryaddress',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
