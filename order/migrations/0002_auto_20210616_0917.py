# Generated by Django 2.2 on 2021-06-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
