from rest_framework import views, generics, response
from .serializers import UserSerializer
from .models import User
from datetime import datetime
from django.db.models import Max, Min, Q


class RegisterUserTime(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# class GetAvailableSlots(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "id"
#     lookup_fields = ("id", "id2")

#     def get_queryset(self):
#         user1 = self.queryset.filter(id=self.kwargs.get(self.lookup_fields[0]))
#         user2 = self.queryset.filter(id=self.kwargs.get(self.lookup_fields[1]))

#         return user1, user2

class GetAvailableSlots(views.APIView):
    def get(self, request, *args, **kwargs):
        interviewer = request.query_params.get("interviewer")
        candidate = request.query_params.get("candidate")
        interviewer_instance = User.objects.filter(id=interviewer).first()
        candidate_instance = User.objects.filter(id=candidate).first()
        start_time = max([interviewer_instance.from_time.strptime("%H:%M %p"), candidate_instance.from_time.strptime("%H:%M %p")])
        print(start_time)
        end_time = min([interviewer_instance.to_time, candidate_instance.to_time])
        for i in range(start_time.hour, end_time.hour, 1):
            print(i)
        return response.Response()


# class GetAvailableSlots(views.APIView):
#     def get(self, request, *args, **kwargs):
#         interviewer = request.query_params.get("interviewer")
#         candidate = request.query_params.get("candidate")
#         from_time = (
#             User.objects.filter(Q(id=interviewer) | Q(id=candidate))
#             .aggregate(Max(datetime.strftime("from_time", "%I:%M %p")))
#             .get("from_time__max")
#         )
#         print(from_time)

#         return response.Response()
