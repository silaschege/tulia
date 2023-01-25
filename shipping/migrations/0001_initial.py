# Generated by Django 4.1.4 on 2023-01-25 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0005_alter_product_product_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserShippingNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('prepare', models.BooleanField(default=False)),
                ('on_transit', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userShippingLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('estate', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('major_landmark', models.CharField(max_length=255)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserShippingItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.product')),
                ('shipping_number', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='shipping.usershippingnumber')),
            ],
        ),
    ]
