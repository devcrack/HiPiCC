from django.db import models
from django.utils import timezone

class Potential(models.Model):
    id_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    potential = models.IntegerField()
    phi = models.FloatField()
    temp = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def execute(self):
        self.created_at = timezone.now()
        self.save()

class DynamicModule(models.Model):
    id_user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    # id_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phi = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def execute(self):
        self.created_at = timezone.now()
        self.save()