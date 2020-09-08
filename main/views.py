from django.shortcuts import redirect
from django.urls import reverse
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
	objs_urls = [i.new_url for i in ShortURL.objects.all()]
	if pk in objs_urls:
		obj = ShortURL.objects.get(new_url=pk)
		return redirect(obj.url)
	else:
		pass
		