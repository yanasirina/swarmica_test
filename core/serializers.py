from rest_framework import serializers

from . import models


class Department(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id', 'name', )


class Author(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('id', 'name', )


class Book(serializers.ModelSerializer):
    author = Author()
    department = Department()

    class Meta:
        model = models.Book
        fields = ('id', 'name', 'author', 'department', 'publishing_year', 'number_of_copies', )


class Client(serializers.ModelSerializer):
    handed_books_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Client
        fields = ('id', 'name', 'handed_books_count')

    def get_handed_books_count(self, instance):
        return instance.handed_books.count()


class ClientHandedBook(serializers.ModelSerializer):
    book = serializers.CharField(source='book.name')

    class Meta:
        model = models.HandedBook
        fields = ('id', 'book', 'handed_date', )


class ClientDetail(serializers.ModelSerializer):
    handed_books = ClientHandedBook(many=True)

    class Meta:
        model = models.Client
        fields = ('id', 'name', 'handed_books', )
