from rest_framework import serializers
from Contents.models import *

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            'name', 'category', 'brand', 'image'
        ]