# Generated by Django 5.0.4 on 2024-05-06 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название продукта')),
                ('model', models.CharField(max_length=100, verbose_name='модель продукта')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('factory', 'factory'), ('retail_network', 'retail_network'), ('sole_trader', 'sole_trader')], max_length=15)),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('email', models.EmailField(max_length=254, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=50, verbose_name='страна')),
                ('city', models.CharField(max_length=40, verbose_name='город')),
                ('street', models.CharField(max_length=60, verbose_name='улица')),
                ('house_number', models.CharField(max_length=10, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='NetworkLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='задолженность')),
                ('time_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_links.product', verbose_name='продукт')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='network_links.supplier', verbose_name='контакты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier', to='network_links.supplier', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'звено сети',
                'verbose_name_plural': 'звенья сети',
                'ordering': ('contacts__name',),
            },
        ),
    ]
