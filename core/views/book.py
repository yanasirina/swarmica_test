from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from utils.pagination import RestPagination
from utils.permissions import DjangoModelPermissions
from .. import models, serializers, filters


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = RestPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (DjangoModelPermissions, )
    queryset = models.Book.objects.order_by('id').select_related('author', 'department')
    serializer_class = serializers.Book
    filterset_class = filters.Book
