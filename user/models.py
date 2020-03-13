from django.conf import settings
from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.

class User(models.Model):
    fist_name = models.CharField(max_length=64, verbose_name='Імʼя')
    last_name = models.CharField(max_length=64, verbose_name='Призвище')
    email = models.EmailField(max_length=128, verbose_name='Електронна почта')
    phone_number = models.CharField(max_length=64, verbose_name='Номер телефона')
    #
    # def __str__(self):
    #     return f'{self.fist_name} {self.last_name}'


class Question(models.Model):
    fist_name = models.CharField(max_length=64, verbose_name='Імʼя', null=True, blank=True)
    last_name = models.CharField(max_length=64, verbose_name='Призвище', null=True, blank=True)
    phone_number = models.CharField(max_length=64, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(max_length=128, verbose_name='Електронна адреса', null=True, blank=True)
    question = models.TextField(verbose_name='Питання', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}'

    class Meta:
        verbose_name = 'Питання'
        verbose_name_plural = 'Питання'


class Service(models.Model):
    service = models.CharField('Назва категорії', max_length=64, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name = 'Категорія послуг'
        verbose_name_plural = 'Категорії послуг'
        ordering = ['service']


class ListService(models.Model):
    category = models.ForeignKey(Service, null=True, on_delete=models.PROTECT, verbose_name='Категорія послуг')
    title = models.CharField('Назва послуги', max_length=128)
    price = models.DecimalField('Вартість', max_digits=10, decimal_places=2, null=True)
    content = models.TextField('Опис', null=True, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, blank=True)
    comment = models.CharField('Коментар', max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Найменування послуги'
        verbose_name_plural = 'Найменування послуг'
