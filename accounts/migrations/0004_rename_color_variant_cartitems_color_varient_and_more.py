# Generated by Django 5.0.3 on 2024-04-02 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cart_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitems',
            old_name='color_variant',
            new_name='color_varient',
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='size_variant',
            new_name='size_varient',
        ),
    ]
