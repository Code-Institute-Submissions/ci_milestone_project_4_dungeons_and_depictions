# Generated by Django 3.1 on 2020-08-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_auto_20200828_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commission',
            name='sku',
            field=models.CharField(blank=True, default='PENDING', max_length=254, null=True),
        ),
    ]
