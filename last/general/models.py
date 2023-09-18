from django.db import models


class Comments(models.Model):

    username = models.CharField('Имя пользователя', max_length=50)
    anons = models.CharField('Немного о себе', max_length=250)
    comment = models.TextField('Комментарий')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):  # Вызывается в момент вывода объекта класса
        return self.username

    class Meta:  # Изменение названия табличек
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
