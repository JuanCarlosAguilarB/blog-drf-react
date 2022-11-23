from django.db import models
from apps.blog.models import Post
# Create your models here.


class Tags(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'tags'

class TagsCategories(models.Model):
    id = models.UUIDField(primary_key=True)
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='post')
    tags = models.ForeignKey(Tags, models.DO_NOTHING, db_column='tags')

    class Meta:
        db_table = 'tags_categories'