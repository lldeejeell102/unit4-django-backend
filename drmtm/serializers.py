from .models import Drmtm
from rest_framework import serializers

class DrmtmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Drmtm
        fields=('name', 'position', 'age', 'height', 'salary')