import django_filters
from django.db.models import Count, F

from . import models


class Book(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    department_name = django_filters.CharFilter(field_name='department__name', lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = models.Book
        fields = '__all__'

    def filter_in_stock(self, queryset, name, value):
        queryset = queryset.annotate(number_of_books_in_stock=F('number_of_copies') - Count('handed_books'))
        if value is True:
            queryset = queryset.filter(number_of_books_in_stock__gt=0)
        elif value is False:
            queryset = queryset.exclude(number_of_books_in_stock__gt=0)
        return queryset
