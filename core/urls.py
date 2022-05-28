from django.urls import path
from .views import RegisterUserTime, GetAvailableSlots

urlpatterns = [
    path("register_time/", RegisterUserTime.as_view()),
    path("available_slots/", GetAvailableSlots.as_view()),
]