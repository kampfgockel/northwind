# Generated by Django 3.1.3 on 2020-11-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('company_name', models.CharField(max_length=40, null=True)),
                ('contact_name', models.CharField(max_length=30, null=True)),
                ('contact_title', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=60, null=True)),
                ('city', models.CharField(max_length=15, null=True)),
                ('region', models.CharField(max_length=15, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=15, null=True)),
                ('phone', models.CharField(max_length=24, null=True)),
                ('fax', models.CharField(max_length=24, null=True)),
            ],
        ),
    ]
