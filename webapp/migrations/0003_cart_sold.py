# Generated by Django 5.0.3 on 2024-03-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='sold',
            field=models.CharField(choices=[('0', '0'), ('1', '1')], default='0', max_length=1),
        ),
    ]
