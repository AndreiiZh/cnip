# Generated by Django 2.2.8 on 2020-01-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20191231_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Питання', 'verbose_name_plural': 'Питання'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service'], 'verbose_name': 'Категорія послуг', 'verbose_name_plural': 'Категорії послуг'},
        ),
        migrations.AddField(
            model_name='listservice',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
