# Generated by Django 5.0.2 on 2024-11-16 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_delete_shoe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]
