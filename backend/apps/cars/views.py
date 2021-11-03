from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(operation_id='List of car', operation_summary='get all'))
class CarListCreateView(ListCreateAPIView):
    """
    get:
        Get all cars
    post:
        Create car
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)
    # filterset_fields = ('year', 'brand', 'model')
    # filterset_class = CarFilter

    # def get_queryset(self):
    #     qs = self.queryset.all()
    #     qs.filter(autopark)
    #     return qs


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
