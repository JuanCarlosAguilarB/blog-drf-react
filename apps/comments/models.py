from django.db import models
from apps.user.models import UserAuth
from apps.blog.models import Post

# Create your models here.
class Comments(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserAuth, models.DO_NOTHING, db_column='user')
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='post')
    comment = models.TextField()

    class Meta:
        db_table = 'comments'
