# Generated by Django 2.2.8 on 2019-12-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191230_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listservice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='Вартість'),
        ),
    ]
