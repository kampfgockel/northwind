# Generated by Django 3.1.3 on 2022-06-14 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
        ('shippers', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(null=True)),
                ('required_date', models.DateField(null=True)),
                ('shipped_date', models.DateField(null=True)),
                ('freight', models.CharField(max_length=24, null=True)),
                ('ship_name', models.CharField(max_length=40, null=True)),
                ('ship_address', models.CharField(max_length=60, null=True)),
                ('ship_city', models.CharField(max_length=15, null=True)),
                ('ship_region', models.CharField(max_length=15, null=True)),
                ('ship_postal_code', models.CharField(max_length=10, null=True)),
                ('ship_country', models.CharField(max_length=15, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employee')),
                ('ship_via', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shippers.shipper')),
            ],
        ),
        migrations.CreateModel(
            name='Order_line',
            fields=[
                ('line', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.product')),
            ],
        ),
    ]
