from rest_framework import routers

from . import views


app_name = 'core'

urlpatterns = []

router = routers.DefaultRouter()
router.register('department', views.DepartmentViewSet, basename='department')
router.register('book', views.BookViewSet, basename='book')

urlpatterns += router.urls
