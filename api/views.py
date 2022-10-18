# https://testdriven.io/blog/drf-views-part-3/


from django.db.models import Max

from rest_framework import generics, permissions, viewsets
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import Actor, Address, City, Country, Film, Language, Category
from .serializers import ActorSerializer, AddressSerializer, CitySerializer, CountrySerializer, FilmSerializer, LanguageSerializer


class ActorList(generics.ListAPIView):
    """
    Return a list with all the actors.
    Allow: GET.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Return a given actor. Only admin users can ger the data.
    Allow: GET, PUT, PATCH, DELETE.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAdminUser, )


class CityViewSet(viewsets.ModelViewSet):
    """
    Provide the following actions:
      - list:     GET
      - create:   POST
      - retrieve: GET
      - update:   PUT | PATCH
      - destroy:  DELETE
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAdminUser, )
    filterset_fields = ['city', 'country']  # e.g. ?country=50


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAdminUser, )


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (permissions.IsAdminUser, )

    @action(detail=False, methods=['get'])  # /min_length
    def min_length(self, request):
        queryset = Film.objects.order_by('length').values()[0]
        return Response(queryset)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAdminUser, )
    filterset_fields = ['name']  # allow e.g. /languages?name=English


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = (permissions.IsAdminUser, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )

    def list(self, request, *args, **kwargs):
        """
        Return a HTML template:
        addresses?format=html
        addresses?format=json
        """
        response = super(AddressViewSet, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response(
                {'data': response.data},
                template_name='api/address_list.html'
            )
        return response


class CategoryList(APIView):
    """Return a HTML template"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api/categories_list.html'

    def get(self, request):
        # Pass the queryset as a variable within the template
        queryset = Category.objects.all()
        return Response({'categories': queryset, 'request': request})