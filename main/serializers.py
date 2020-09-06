from rest_framework_json_api import serializers

from .models import ShortURL


class URLSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortURL
        fields = ['url', 'custom_url']