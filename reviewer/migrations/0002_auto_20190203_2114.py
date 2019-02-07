# Generated by Django 2.1.5 on 2019-02-03 21:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateMyProfSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('professor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='redditSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='RateMyProfPage',
        ),
        migrations.AddField(
            model_name='professor',
            name='lastUpdated',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 3, 21, 14, 1, 664423, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='redditsnapshot',
            name='Reviews',
            field=models.ManyToManyField(to='reviewer.Review'),
        ),
        migrations.AddField(
            model_name='ratemyprofsnapshot',
            name='reviews',
            field=models.ManyToManyField(to='reviewer.Review'),
        ),
        migrations.AddField(
            model_name='professor',
            name='ratingPages',
            field=models.ManyToManyField(to='reviewer.RateMyProfSnapshot'),
        ),
    ]
