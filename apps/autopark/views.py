from apps.cars.serializers import CarSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import AutoParkModel
from .serializers import AutoParkSerializer


class AutoParkListView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class AutoParkRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()

    def perform_create(self, serializer):
        autopark = self.get_object()
        serializer.save(autopark=autopark)
