# Generated by Django 2.0.1 on 2018-01-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotify_id', models.CharField(max_length=64)),
                ('acousticness', models.FloatField()),
                ('analysis_url', models.URLField()),
                ('danceability', models.FloatField()),
                ('duration_ms', models.IntegerField()),
                ('energy', models.FloatField()),
                ('instrumentalness', models.FloatField()),
                ('key', models.IntegerField()),
                ('liveness', models.FloatField()),
                ('loudness', models.FloatField()),
                ('mode', models.IntegerField()),
                ('speechiness', models.FloatField()),
                ('tempo', models.FloatField()),
                ('time_signature', models.IntegerField()),
                ('track_href', models.URLField()),
                ('valence', models.FloatField()),
            ],
        ),
    ]