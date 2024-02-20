import django_filters

from . import models


class Book(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    department_name = django_filters.CharFilter(field_name='department__name', lookup_expr='icontains')

    class Meta:
        model = models.Book
        fields = '__all__'
