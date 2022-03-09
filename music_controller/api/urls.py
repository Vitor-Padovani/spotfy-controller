from django.urls import path
from .views import RoomView

# secondary url redirector
urlpatterns = [
    path('room', RoomView.as_view()),
]
