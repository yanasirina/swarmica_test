from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Отдел библиотеки'
        verbose_name_plural = 'Отделы библиотеки'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Имя', max_length=255)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Имя', max_length=255)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.PROTECT, related_name='books')
    department = models.ForeignKey(Department, verbose_name='Отдел', on_delete=models.PROTECT, related_name='books')
    publishing_year = models.PositiveSmallIntegerField('Год издания')
    number_of_copies = models.PositiveSmallIntegerField('Количество экземпляров')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'{self.author}: "{self.name}" ({self.publishing_year}г.)'
