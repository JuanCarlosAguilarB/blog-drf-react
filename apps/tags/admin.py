from django.contrib import admin
from apps.tags import models
# Register your models here.

admin.site.register(models.Tags)
admin.site.register(models.TagsCategories)

