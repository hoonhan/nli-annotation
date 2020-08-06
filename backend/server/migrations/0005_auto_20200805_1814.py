# Generated by Django 3.0.8 on 2020-08-05 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20200805_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='time',
            new_name='joinTime',
        ),
        migrations.RemoveField(
            model_name='user',
            name='postSurveyDone',
        ),
        migrations.AddField(
            model_name='user',
            name='instrEndTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='instrStartTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='preEndTime',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]