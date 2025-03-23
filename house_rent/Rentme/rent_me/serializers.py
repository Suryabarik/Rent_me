from rest_framework import serializers
from .models import User, Seller, Property, PGDetails, RoomDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class PGDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PGDetails
        fields = '__all__'

class RoomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomDetails
        fields = '__all__'
