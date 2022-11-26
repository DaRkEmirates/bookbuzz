# Generated by Django 2.2.1 on 2019-06-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]