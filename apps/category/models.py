from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    
    name = models.CharField(max_length=255, unique=True)
    thumbnail =         models.ImageField(upload_to='media/categories/')

    def __str__(self):
        return self.name

    # para obtener el url de la imagen
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''