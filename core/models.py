from django.db import models

class User(models.Model):
    USER_TYPES = ((1, "Interviewer"), (2, "Candidate"))
    user_type = models.IntegerField(choices=USER_TYPES)
    from_time = models.TimeField()
    to_time = models.TimeField()
