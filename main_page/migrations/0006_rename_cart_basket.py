# Generated by Django 4.2 on 2023-04-28 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_cart_delete_basket'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart',
            new_name='Basket',
        ),
    ]
