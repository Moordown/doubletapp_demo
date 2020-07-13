from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer, LevelSerializer, ThemeSerializer, WordSerializer, ShortThemeSerializer
from .models import Category, Level, Theme, Word
from .decorators import check_secret


@api_view(['GET'])
@check_secret
def category_list(request):
    objects = Category.objects.all().filter()
    serializer = CategorySerializer(objects, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@check_secret
def level_list(request):
    objects = Level.objects.all().filter()
    serializer = LevelSerializer(objects, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@check_secret
def themes_list_by_pk(request, pk):
    try:
        object = Theme.objects.get(pk=pk)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ShortThemeSerializer(object)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@check_secret
def themes_list_by_level_and_category(request):
    level = request.GET.get('level')
    category = request.GET.get('category')
    if level is None or category is None:
        return Response('You should pass "level" and "category" via query params', status=status.HTTP_400_BAD_REQUEST)
    objects = Theme.objects.filter(level=level).filter(category=category)
    serializer = ThemeSerializer(objects, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@check_secret
def words_list_by_id(request, pk):
    try:
        object = Word.objects.get(pk=pk)
    except Theme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = WordSerializer(object)
    return JsonResponse(serializer.data, safe=False)
