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
