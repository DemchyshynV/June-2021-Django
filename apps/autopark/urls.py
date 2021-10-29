from django.urls import path

from .views import AutoParkAddCarView, AutoParkListView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view()),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view())
]
