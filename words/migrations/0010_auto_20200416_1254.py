# Generated by Django 2.2.11 on 2020-04-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0009_auto_20190605_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='word',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-04-16-12.54.53', max_length=100),
        ),
    ]
