from rest_framework import routers
from .views import *
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user_pro')
router.register(r'cartitem', CartItemViewSet, basename='cartitem')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'sparepart', SparePartViewSet, basename='sparepart')
router.register(r'carmodel', CarModelViewSet, basename='carmodel')

urlpatterns = [
    path('', include(router.urls)),
    path('car/', CarAPIView.as_view(), name='cars'),
    path('car/<int:pk>/', CarWideAPIView.as_view(), name='car_wide'),
    path('create_car/', CarCreateAPIView.as_view(), name='cars_create'),
    path('comment/', CommentAPIView.as_view(), name='comment_car'),
    path('spare/', SpareAPIView.as_view(), name='spare_list'),
    path('spare/<int:pk>/', SpareWideAPIView.as_view(), name='spare_wide'),
    path('spare_create/', SpareCreateAPIView.as_view(), name='spare_created'),
    path('users/', UserProfileCreteAPIView.as_view(), name='user_create'),
    path('image_car/', ImageCarCreateAPIView.as_view(), name='image_car_create'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]

