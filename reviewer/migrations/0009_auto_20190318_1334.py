# Generated by Django 2.1.5 on 2019-03-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0008_auto_20190317_1838'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RateMyProfSnapshot',
            new_name='ReviewSnapshot',
        ),
        migrations.RenameField(
            model_name='reviewsnapshot',
            old_name='url',
            new_name='rmp_url',
        ),
        migrations.AddField(
            model_name='review',
            name='source',
            field=models.CharField(default='ratemyprofessor', max_length=20),
            preserve_default=False,
        ),
    ]
