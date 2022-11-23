from django.db import models
import uuid
from django.utils import timezone
from apps.category.models import Category
from apps.user.models import UserAuth
# Create your models here.


def blog_directory_path(instance, filename):
    """función asignar la ubicación de las imagenes en la carpeta correspondiente
    """
    return 'blog/{0}/{1}'.format(instance.title, filename)



class Post(models.Model):

    class PostObjects(models.Manager):
        """clase que permite traer todos los blogs publicados"""
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    blog_uuid =         models.UUIDField(default=uuid.uuid4, unique=True)
    title =             models.CharField(max_length=255)
    slug =              models.SlugField(unique=True)
    thumbnail =         models.ImageField(upload_to=blog_directory_path, blank=True, null=True)
    video =             models.FileField(upload_to=blog_directory_path, blank=True, null=True)
    content =           models.TextField()
    excerpt =           models.CharField(max_length=100)

    author =            models.ForeignKey(UserAuth, models.DO_NOTHING, db_column='user')
    category =          models.ManyToManyField(Category)
    

    published =         models.DateTimeField(default=timezone.now)

    # siempre que se cree un blog va a estar con status draf, por defecto
    status =            models.CharField(max_length=10, choices=options, default='draft')

    objects =           models.Manager()  # default manager
    postobjects =       PostObjects()  # custom manager

    class Meta:
        # estamso ordenando los post por fecha descendente
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_video(self):
        if self.video:
            return self.video.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''
    

class Likes(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(UserAuth, models.DO_NOTHING, db_column='user')
    post = models.ForeignKey(Post, models.DO_NOTHING, db_column='post')

    class Meta:
        db_table = 'likes'
