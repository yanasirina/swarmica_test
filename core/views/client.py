from rest_framework import viewsets, exceptions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from utils.pagination import RestPagination
from utils.permissions import DjangoModelPermissions
from .. import models, serializers
from ..services import give_book_to_client, return_book_from_client, BookIsNotAvailable


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

    @action(detail=True, methods=['get'], url_path=r'take_book/(?P<book_id>\w+)')
    def take_book(self, request, pk: str, book_id: str):
        client, book = self._get_client_and_book(client_id=pk, book_id=book_id)

        try:
            give_book_to_client(book=book, client=client)
        except BookIsNotAvailable as err:
            raise exceptions.ValidationError({'detail': str(err)})

        return Response({'detail': 'success'})

    @action(detail=True, methods=['get'], url_path=r'return_book/(?P<book_id>\w+)')
    def return_book(self, request, pk: str, book_id: str):
        client, book = self._get_client_and_book(client_id=pk, book_id=book_id)

        try:
            return_book_from_client(book=book, client=client)
        except BookIsNotAvailable as err:
            raise exceptions.ValidationError({'detail': str(err)})

        return Response({'detail': 'success'})

    def _get_client_and_book(self, client_id, book_id) -> tuple[models.Client, models.Book]:
        try:
            client = models.Client.objects.get(pk=client_id)
            book = models.Book.objects.get(pk=book_id)
        except models.Client.DoesNotExist:
            raise exceptions.NotFound({'detail': 'client does not exist'})
        except models.Book.DoesNotExist:
            raise exceptions.NotFound({'detail': 'book does not exist'})

        return client, book
