from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AirPlaneModel
from .serializers import AirPlaneSerializer


class AirPlaneListCreateView(APIView):
    def get(self, *args, **kwargs):
        airplanes = AirPlaneModel.objects.all()
        speed = self.request.query_params.get('speed')
        if speed:
            airplanes = airplanes.filter(speed__gte=speed)
        serializer = AirPlaneSerializer(airplanes, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AirPlaneSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class AirPlaneRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AirPlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        serializer = AirPlaneSerializer(airplane)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = AirPlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        serializer = AirPlaneSerializer(airplane, data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = AirPlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        serializer = AirPlaneSerializer(airplane, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AirPlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        airplane = AirPlaneModel.objects.get(pk=pk)
        airplane.delete()
        return Response(status.HTTP_204_NO_CONTENT)
