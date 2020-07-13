from django.urls import path, include
from polls import views


urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('levels/', views.level_list, name='levels'),
    path('themes/<int:pk>/', views.themes_list_by_pk, name='themes_list_by_pk'),
    path('themes/', views.themes_list_by_level_and_category, name='themes_list_by_level_and_category'),
    path('words/', views.words_list, name='words_list'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
