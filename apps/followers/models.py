from django.db import models

from apps.user.models import UserAuth

class Following(models.Model):
    id = models.UUIDField(primary_key=True)
    follower = models.ForeignKey(UserAuth, models.DO_NOTHING, db_column='follower', related_name='follower')
    following = models.ForeignKey(UserAuth, models.DO_NOTHING, db_column='following', related_name='following')

    class Meta:
        db_table = 'following'