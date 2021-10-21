from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveDestroyAPIView

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from cars.serializers import CarSerializer


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
        autopark = self.get_object()
        serializer.save(autopark=autopark)
