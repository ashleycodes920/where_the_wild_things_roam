# Generated by Django 3.1.2 on 2020-10-14 21:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistPlatform',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_gallery.artist')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_gallery.platform')),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_platforms',
            field=models.ManyToManyField(related_name='_artist_artist_platforms_+', to='art_gallery.ArtistPlatform'),
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('thumbnail_url', models.CharField(max_length=300, null=True)),
                ('media_url', models.CharField(max_length=300)),
                ('remote_id', models.CharField(max_length=80, null=True)),
                ('artists', models.ManyToManyField(to='art_gallery.Artist')),
                ('remote_platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='art_gallery.platform')),
            ],
        ),
    ]
