# Generated by Django 2.0 on 2018-04-25 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_available',
            field=models.BooleanField(default=True, verbose_name='Available'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_stock',
            field=models.PositiveIntegerField(verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated'),
        ),
    ]
