# Generated by Django 3.0.8 on 2020-08-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_auto_20200805_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Baseline'), (1, 'Artificial'), (2, 'Natural')], default=0),
        ),
    ]