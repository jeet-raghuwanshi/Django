from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class tag(models.Model):
    label = models.CharField(max_length=255)


class taggeditem(models.Model):
    #what tag applied to what object
    tag=models.ForeignKey(tag, on_delete=models.CASCADE)
    # type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()