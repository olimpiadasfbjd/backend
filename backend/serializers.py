from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
	    model = Data
	    fields = ('id','tension','current', 'wind_speed', 'wind_direction')