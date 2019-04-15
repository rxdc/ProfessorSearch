# Generated by Django 2.1.5 on 2019-04-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0010_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.CharField(default='Default University', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text_hash',
            field=models.CharField(default=1234567890, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]