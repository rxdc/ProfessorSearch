# Generated by Django 2.1.5 on 2019-02-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewer', '0003_professor_hitcounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='school',
            field=models.CharField(max_length=100),
        ),
    ]
