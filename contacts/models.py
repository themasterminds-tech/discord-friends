from django.db import models
from django.contrib.auth.models import User


class Friends(models.Model):
    user_id = models.CharField(max_length=18,
                               verbose_name='Discord User ID', default='000000000000000000', null=False, blank=False)
    username = models.CharField(max_length=1024,
                                verbose_name='Discord Username', default="WumpusLand", null=False, blank=False)
    tag = models.CharField(verbose_name='Discord Tag', null=False,
                           blank=False, default="0123", max_length=4)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.username)

    class Meta:
        verbose_name_plural = 'Friends'
