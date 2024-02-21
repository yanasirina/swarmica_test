from datetime import date

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


class Client(models.Model):
    name = models.CharField('Имя', max_length=255)

    class Meta:
        verbose_name = 'Посетитель библиотеки'
        verbose_name_plural = 'Посетители библиотеки'

    def __str__(self):
        return self.name


class HandedBook(models.Model):
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.PROTECT, related_name='handed_books')
    client = models.ForeignKey(Client, verbose_name='Посетитель', on_delete=models.PROTECT, related_name='handed_books')
    handed_date = models.DateField('Дата взятия', default=date.today)

    class Meta:
        verbose_name = 'Взятая на руки книга'
        verbose_name_plural = 'Взятые на руки книги'

    def __str__(self):
        return f'{self.book} ({self.handed_date})'
