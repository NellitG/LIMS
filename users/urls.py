from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users', UserListCreateAPIView.as_view()),
    path('users/<uuid:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
]
