from .models import Drmtm
from rest_framework import serializers

class DrmtmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Drmtm
        field=('name', 'position', 'age', 'height', 'salary')