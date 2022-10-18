from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ActorList, AddressViewSet, ActorDetail, CityViewSet, CountryViewSet, FilmViewSet, LanguageViewSet, CategoryList


router = DefaultRouter()
router.register('cities', CityViewSet, basename='cities')
router.register('countries', CountryViewSet, basename='countries')
router.register('films', FilmViewSet, basename='films')
router.register('languages', LanguageViewSet, basename='languages')
router.register('addresses', AddressViewSet, basename='addresses')


urlpatterns = [
    path('actors/', ActorList.as_view(), name='actor_list'),
    path('actors/<int:pk>', ActorDetail.as_view(), name='actor_detail'),
    path('', include(router.urls)),
    path('categories/', CategoryList.as_view(), name='category_list'),
]