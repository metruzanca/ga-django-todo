from rest_framework import serializers
from .models import User, List, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('__all__')

    # override default function to add items to the list when we get a given list
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = ItemSerializer(instance.items.all(), many=True).data
        return representation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
