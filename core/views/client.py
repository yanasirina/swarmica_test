from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from utils.pagination import RestPagination
from utils.permissions import DjangoModelPermissions
from .. import models, serializers


class ClientViewSet(viewsets.ModelViewSet):
    pagination_class = RestPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (DjangoModelPermissions, )
    queryset = models.Client.objects.order_by('id').prefetch_related('handed_books')
    serializer_class = serializers.Client

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ClientDetail
        return super().get_serializer_class()
