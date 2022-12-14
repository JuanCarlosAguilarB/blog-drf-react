from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
    id = models.UUIDField(primary_key=True)
    # parent = models.ForeignKey(
    #     'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    thumbnail =         models.ImageField(upload_to='media/categories/',null=True, blank=True)

    def __str__(self):
        return self.name

    # para obtener el url de la imagen
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''