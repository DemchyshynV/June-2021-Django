from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from .models import CarModel
from .serializers import CarSerializer, Car2Serializer


# class UserListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.filter(year__in=[2000, 2010, 1980])
#         # cars = cars.filter(model__iendswith='34').order_by()
#         # cars = CarModel.objects.filter(model__iendswith='34').order_by('-brand')[1:5]
#         cars = CarModel.objects.filter(model__iendswith='34').order_by('-brand').exclude(year=2006)
#         serializer = CarSerializer(instance=cars, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class UserRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response('Car with this id is not found', status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         serializer = Car2Serializer(instance=car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         data = self.request.data
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response('Car with this id is not found', status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         # serializer = CarSerializer(instance=car, data=data, partial=True)
#         serializer = CarSerializer(instance=car, data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get('pk')
#         exists = CarModel.objects.filter(pk=pk).exists()
#         if not exists:
#             return Response('User with this id is not found', status.HTTP_404_NOT_FOUND)
#         car = CarModel.objects.get(pk=pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class UserListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        qs = CarModel.objects.all()
        if year:
            qs = qs.filter(year__gte=year)
        return qs

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
