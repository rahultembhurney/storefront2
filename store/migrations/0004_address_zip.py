# Generated by Django 4.0.3 on 2022-04-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slugfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
