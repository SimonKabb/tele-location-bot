from django.db import models


class UserLocation(models.Model):
    user_id = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id}: {self.latitude}, {self.longitude}"
