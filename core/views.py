from datetime import datetime
from rest_framework import views, status, response
from .serializers import UserSerializer
from .models import User


class RegisterUserTime(views.APIView):
    def post(self, request, *args, **kwargs):
        user_type = request.data.get("user_type")
        from_time = request.data.get("from_time")
        to_time = request.data.get("to_time")

        from_time = datetime.strptime(from_time, "%I:%M %p").time()
        to_time = datetime.strptime(to_time, "%I:%M %p").time()

        user = User.objects.create(
            user_type=user_type, from_time=from_time, to_time=to_time
        )
        seriazlier = UserSerializer(instance=user)

        return response.Response(data=seriazlier.data)


class GetAvailableSlots(views.APIView):
    def get(self, request, *args, **kwargs):
        interviewer = request.query_params.get("interviewer")
        candidate = request.query_params.get("candidate")

        interviewer_instance = User.objects.filter(id=interviewer).first()
        candidate_instance = User.objects.filter(id=candidate).first()

        if not interviewer_instance or not candidate_instance:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

        # select max from start time and min from end time of both interviewer and candidate
        from_time = max([interviewer_instance.from_time, candidate_instance.from_time])
        to_time = min([interviewer_instance.to_time, candidate_instance.to_time])

        time_available = []
        for i in range(from_time.hour, to_time.hour, 1):
            time_available.append((i, i + 1))

        return response.Response({"Time avalailable": time_available})
