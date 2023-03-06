from rest_framework import serializers, status
from .models import *



class menuSerializer(serializers.ModelSerializer):

    class Meta:
        model = menu
        fields = '__all__'



class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'


