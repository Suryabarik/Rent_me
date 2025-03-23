from django.shortcuts import render

from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Seller, Property
from .serializers import UserSerializer, SellerSerializer, PropertySerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

# ==========================
# User & Seller Registration
# ==========================

class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))

class SellerSignupView(CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))

# ==========================
# User & Seller Login
# ==========================

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    # Check in User model
    user = User.objects.filter(email=email).first()
    if user and check_password(password, user.password):
        return Response({'message': 'User login successful', 'user_id': user.user_id}, status=status.HTTP_200_OK)

    # Check in Seller model
    seller = Seller.objects.filter(email=email).first()
    if seller and check_password(password, seller.password):
        return Response({'message': 'Seller login successful', 'seller_id': seller.seller_id}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# ==========================
# Property Management
# ==========================
'''
class PropertyCreateView(CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
'''



# ✅ Create Property (POST) & List Properties (GET)
class PropertyListCreateView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ Retrieve, Update, and Delete a Specific Property (GET, PUT, DELETE)
class PropertyDetailView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        property_instance = get_object_or_404(Property, pk=pk)
        serializer = PropertySerializer(property_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        property_instance = get_object_or_404(Property, pk=pk)
        serializer = PropertySerializer(property_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        property_instance = get_object_or_404(Property, pk=pk)
        property_instance.delete()
        return Response({'message': 'Property deleted successfully'}, status=status.HTTP_204_NO_CONTENT)





# ==========================
# Property Booking (Mock)
# ==========================

@api_view(['POST'])
def book_property(request, property_id):
    property_instance = Property.objects.filter(id=property_id).first()
    
    if not property_instance:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    # Mock booking logic (Just marking it as unavailable)
    property_instance.availability = "Booked"
    property_instance.save()
    
    return Response({'message': 'Property booked successfully'}, status=status.HTTP_200_OK)

