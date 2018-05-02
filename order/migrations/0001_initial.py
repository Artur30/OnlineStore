# Generated by Django 2.0 on 2018-05-02 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_auto_20180425_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('order_last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('order_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('order_address', models.CharField(max_length=300, verbose_name='Address')),
                ('order_postal_code', models.CharField(max_length=20, verbose_name='Postal code')),
                ('order_city', models.CharField(max_length=50, verbose_name='City')),
                ('order_created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('order_updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('order_paid', models.BooleanField(default=False, verbose_name='Paid')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'order',
                'ordering': ('-order_created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('order_item_quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('order_item_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.Order')),
                ('order_item_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.Product')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]