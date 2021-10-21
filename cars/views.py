from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializers import CarSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    def get_queryset(self):
        year = self.request.query_params.get('year')
        auto_park_id = self.request.query_params.get('autoParkId')
        qs = self.queryset.all()
        if year:
            qs = qs.filter(year__gte=year)
        if auto_park_id:
            qs = qs.filter(autopark_id=auto_park_id)
        return qs


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
