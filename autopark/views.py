from rest_framework.generics import ListAPIView, CreateAPIView

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from cars.serializers import CarSerializer


class AutoParkListView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCar(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        # pk = self.kwargs.get('pk')
        autopark = self.get_object()
        serializer.save(autopark=autopark)
