from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        auto_park = self.get_object()
        serializer.save(autopark=auto_park)
