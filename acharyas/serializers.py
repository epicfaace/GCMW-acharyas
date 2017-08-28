from .models import Acharya, Centre
from rest_framework import serializers

class AcharyaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acharya
        fields = ('salutation', 'name', 'centre')


class CentreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Centre
        fields = ('name', 'address_line_1')