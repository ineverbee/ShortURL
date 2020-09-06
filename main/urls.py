from django.urls import include, path
from rest_framework import routers

from .views import URLViewset, url_redirect

api_router = routers.SimpleRouter()
api_router.register('', URLViewset, basename='urls')

urlpatterns = [
    #path('', url_redirect),
    path(r'<str:pk>/', url_redirect)
]

urlpatterns += api_router.urls