from .models import Acharya, Centre
from rest_framework import serializers

class AcharyaSerializerShort(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acharya
        fields = ('id', '__str__', 'url')

class CentreSerializer(serializers.HyperlinkedModelSerializer):
    acharya = AcharyaSerializerShort(many=True, read_only=True)
    class Meta:
        model = Centre
        fields = ('name', 'address_line_1', 'acharya')

class CentreSerializerShort(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Centre
        fields = ('id', '__str__', 'url')

class AcharyaSerializer(serializers.HyperlinkedModelSerializer):
    #centre = serializers.StringRelatedField(many=True)
    centre = CentreSerializerShort(many=True, read_only=True)
    class Meta:
        model = Acharya
        fields = ('salutation', 'name', 'centre')
