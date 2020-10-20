from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'img_url', )
        model = Item


