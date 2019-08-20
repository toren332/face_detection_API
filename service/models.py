from django.contrib.auth.models import User
from django.db import models
from .ML import edited_img
from django.core.files.base import ContentFile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.files import File


class Obj(models.Model):
    original_photo = models.ImageField(upload_to='original/')
    edited_photo = models.ImageField(upload_to='edited/')

    def __str__(self):
        return self.original_photo.name

@receiver(post_save, sender=Obj)
def print_only_after_deal_created(sender, instance, created, **kwargs):

    if created:
        instance.edited_photo.name = edited_img(instance.original_photo.name)
        instance.save()


class FaceBorder(models.Model):
    obj = models.ForeignKey(Obj, on_delete=models.CASCADE)
    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    w = models.PositiveIntegerField()
    h = models.PositiveIntegerField()





