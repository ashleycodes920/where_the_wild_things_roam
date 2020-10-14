from django.db import models
import uuid


class Art(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    description = models.TextField()
    thumbnail_url = models.CharField(max_length=300, null=True)
    media_url = models.CharField(max_length=300)
    remote_id = models.CharField(max_length=80, null=True)
    remote_platform = models.ForeignKey("Platform", on_delete=models.CASCADE)
    artists = models.ManyToManyField("Artist")


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist_platforms = models.ManyToManyField("ArtistPlatform", related_name="+")


class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)


class ArtistPlatform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

