from django.http import JsonResponse
from rest_framework import serializers

from .models import Category, Level, Theme, Word


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ['id', 'name', 'code']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name', 'translation', 'transcription', 'example', 'sound']


class ShortWordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'name']


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    words = ShortWordSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ['id', 'category', 'level', 'name', 'photo', 'words']


class ShortThemeSerializer(serializers.HyperlinkedModelSerializer):
    level = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Theme
        fields = ['id', 'category', 'level', 'name', 'photo']
