from django.db import models

STATUS_CHOICES = [
    ('New', 'new'),
    ('In progress', 'in_progress'),
    ('Done', 'done')
]


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=40, null=True, blank=True, default='Unknown', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')


class Issue(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', null=False, blank=False, verbose_name='Статус')
    finish_date = models.DateField(null=True, default='', verbose_name='Дата выполнения')

