# Generated by Django 3.1.2 on 2021-01-03 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210103_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_name', models.CharField(blank=True, max_length=50, null=True)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Drug',
                'verbose_name_plural': 'Drugs',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=50, null=True)),
                ('order_name', models.CharField(blank=True, max_length=50, null=True)),
                ('order_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('order_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('order_quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('order_price', models.CharField(blank=True, max_length=50, null=True)),
                ('added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('test_number', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('test_date', models.DateTimeField(blank=True, null=True)),
                ('test_type', models.CharField(blank=True, choices=[('B', 'BLOOD'), ('C', 'CORONA')], max_length=50, null=True)),
                ('added', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.websiteuser')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
            },
        ),
    ]
