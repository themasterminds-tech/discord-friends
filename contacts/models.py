from django.db import models


class Friends(models.Model):
    user_id = models.CharField(max_length=255, unique=True,
                               verbose_name='Discord User ID', default='000000000000000000', null=False, blank=False)
    username = models.CharField(max_length=255, unique=True,
                                verbose_name='Discord Username', default="WumpusLand", null=False, blank=False)
    tag = models.CharField(verbose_name='Discord Tag', null=False,
                           blank=False, default="0123", max_length=4)

    def __str__(self) -> str:
        return str(self.username)

    class Meta:
        verbose_name_plural = 'Friends'
