from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Property, CustomUser
from .serializers import PropertySerializer, RegisterSerializer


class ObtainAuthToken(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def ApiOverview(request):
    api_urls = {
        'List': '/property/list/',
        'Detail View': '/property/detail/<str:pk>/',
        'Create': '/property/create/',
        'Update': '/property/update/<str:pk>/',
        'Delete': '/property/delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_property(request):
    propertyS = PropertySerializer(data=request.data)
    try:
        # Validate existing data
        if Property.objects.filter(**request.data).exists():
            raise serializers.ValidationError('Property already exists')

        if propertyS.is_valid():
            propertyS.save()
            return Response(status=status.HTTP_201_CREATED, data='Property created successfully')
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data=propertyS.errors)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_property(request):
    try:
        if request.query_params:
            properties = Property.objects.filter(**request.query_params.dict())
        else:
            properties = Property.objects.all()

        if properties:
            property_serializer = PropertySerializer(properties, many=True)
            return Response(property_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data='No properties found')
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([AllowAny])
def detail_property(request, pk):
    try:
        property = Property.objects.get(id=pk)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Property not found')

    propertyS = PropertySerializer(property, many=False)
    return Response(propertyS.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_property(request, pk):
    try:
        property_instance = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        serializer = PropertySerializer(instance=property_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data='Property updated successfully')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_property(request, pk):
    try:
        property_instance = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        property_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT, data='Property deleted successfully')
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
