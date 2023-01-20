# Generated by Django 4.1.4 on 2023-01-18 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productsubcategory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.productsubcategory'),
        ),
    ]
