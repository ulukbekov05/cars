from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'make_car':['exact'],
            'category':['exact'],
            'year': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }