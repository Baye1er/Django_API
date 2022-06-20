from rest_framework import serializers
from .models import Restau


class RestauListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restau
        fields = [
            'id',
            'restau_name',
            'street',
            'city',
            'zip_code',
        ]


class RestauDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restau
        fields = [
            'id',
            'restau_name',
            'street',
            'city',
            'zip_code',
            'website',
            'phone_number',
            'description',
            'email',
            'active'
        ]
