from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Товар')
    price = models.IntegerField(verbose_name='Цена товара')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО клиента')
    age = models.IntegerField(verbose_name='Возраст клиента')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    date_purchase = models.DateTimeField('Дата покупки')

    def __str__(self):
        return self.name