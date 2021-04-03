from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


routeur = DefaultRouter()
routeur.register('tags', views.TagViewSet)
routeur.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(routeur.urls)),
]
