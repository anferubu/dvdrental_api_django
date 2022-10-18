from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Actor, Address, City, Country, Film, Language


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    # Convert foreign key in a hyperlink to detail view
    country = serializers.HyperlinkedRelatedField(
        view_name='countries-detail', many=False, read_only=True
    )
    class Meta:
        model = City
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    """
    If city has the field country. We can use the field city_set to bring all
    asociated cities to a country. This is a reverse relationship.
    """
    # Bring a specific field of the relationship
    city_set = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='city'
    )
    # Apply a unique validator to the country field
    country = serializers.CharField(
        max_length=50,
        validators=[UniqueValidator(queryset=Country.objects.all())]
    )
    class Meta:
        model = Country
        fields = ('country_id', 'country', 'city_set')


class LanguageSerializer(serializers.ModelSerializer):
    # Change the format of the last_update field
    last_update = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = Language
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    # Convert the foreign key to the entire object it represents
    language = LanguageSerializer(many=False, read_only=True)
    class Meta:
        model = Film
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    # Convert the foreign key to the field object indicated
    city = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='city'
    )
    class Meta:
        model = Address
        fields = '__all__'