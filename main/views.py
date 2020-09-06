from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import ShortURL
from .serializers import URLSerializer


class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()


class URLViewset(BaseViewSet):
    serializer_class = URLSerializer
    model = ShortURL


def url_redirect(request, pk=None):
	if pk == None:
		pass
	else:
		obj = ShortURL.objects.get(custom_url=pk)
		return redirect(obj.url)
		