# Generated by Django 2.2.8 on 2020-01-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_listservice_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listservice',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Коментар'),
        ),
    ]