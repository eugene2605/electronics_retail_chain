# Generated by Django 5.0.4 on 2024-05-07 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networklink',
            name='debt_to_supplier',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='задолженность'),
        ),
    ]
