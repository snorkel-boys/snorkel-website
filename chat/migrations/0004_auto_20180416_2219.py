# Generated by Django 2.0.4 on 2018-04-16 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_mask'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='cnt_member',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
