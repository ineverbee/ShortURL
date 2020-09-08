from django.urls import include, path
from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework import routers

from .views import URLViewset, url_redirect

api_router = routers.SimpleRouter()
api_router.register('', URLViewset, basename='urls')
api_router.register('url', URLViewset, basename='urls')

urlpatterns = [
    path(r'<str:pk>/', url_redirect),
    url(r'^favicon\.ico$', RedirectView.as_view(url='https://www.flaticon.com/free-icon/link_2463007?term=link&page=1&position=60'), name='favicon')
]

urlpatterns += api_router.urls