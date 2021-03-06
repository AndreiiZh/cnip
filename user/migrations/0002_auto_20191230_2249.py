# Generated by Django 2.2.8 on 2019-12-30 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Категорія послуг', 'verbose_name_plural': 'Категорії послуг'},
        ),
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(db_index=True, max_length=64, verbose_name='Назва категорії'),
        ),
        migrations.CreateModel(
            name='ListService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Назва послуги')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Вартість')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='user.Service', verbose_name='Категорія послуг')),
            ],
            options={
                'verbose_name': 'Найменування послуги',
                'verbose_name_plural': 'Найменування послуг',
            },
        ),
    ]
