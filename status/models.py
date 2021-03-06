from django.db import models
from django.conf import settings


def upload_status_image(instance, filename):
    return f"updates/{instance.user}/{filename}"

class StatusQuerySet(models.QuerySet):
    pass 

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

# Create your models here.
class Status(models.Model): #similar to fb status, instagram post, tweet, linkdein post
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(null=True, blank=True)
    image       = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    update_at   = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = StatusManager()

    def __str__(self):
        return str(self.content)[:50] 

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'