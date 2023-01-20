# Generated by Django 4.1.4 on 2023-01-17 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_sub_category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=255)),
                ('product_price', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('product_image', models.ImageField(default='media/', upload_to='product_images/')),
                ('merchant', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='user.merchantbiodata')),
            ],
        ),
    ]
