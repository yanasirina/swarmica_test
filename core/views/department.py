from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from utils.pagination import RestPagination
from utils.permissions import DjangoModelPermissions
from .. import models, serializers


class DepartmentViewSet(viewsets.ModelViewSet):
    pagination_class = RestPagination
    authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (DjangoModelPermissions, )
    queryset = models.Department.objects.order_by('id')
    serializer_class = serializers.Department
