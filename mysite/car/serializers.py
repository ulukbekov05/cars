from rest_framework import serializers
from .models import (
    UserProfile, CartItem, Cart, Category, SpareParts, Spare,
    CommitCar, Car, CarModel, CarMake, Network, ImageCar, Phone
)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = '__all__'

class SpareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields = ['id', 'spares_name']


class SpareWideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields =['spares_name', 'spares', 'category', 'users',
                 'description', 'price', 'created_at', 'spare_cars', 'phone' ]


class SpareCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spare
        fields ='__all__'


class CommitCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommitCar
        fields = '__all__'


class ImageCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = ['image_car']

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phone']

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['network', 'network_link', 'title']


class CarSerializer(serializers.ModelSerializer):
    image_cars = ImageCarSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = ['id','car_make', 'category', 'price', 'image_cars']

class CarWideSerializer(serializers.ModelSerializer):
    image_cars = ImageCarSerializer(many=True, read_only=True)
    number_user = PhoneSerializer(many=True, read_only=True)
    network_cars = NetworkSerializer(many=True, read_only=True)
    data = serializers.DateTimeField(format=('%d-%m-%Y'))
    class Meta:
        model = Car
        fields = ['car_make', 'category', 'make_car', 'user', 'year', 'cash',
                  'color', 'description', 'price', 'rule', 'mileage', 'fuel',
                  'video_car', 'data', 'image_cars', 'number_user',
                  'network_cars']

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    image_cars = ImageCarSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = '__all__'


class ImageCarCreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCar
        fields = '__all__'



