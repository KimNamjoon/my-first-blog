# Generated by Django 2.2.2 on 2019-06-04 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='examples',
            field=models.CharField(default='nil', max_length=1000),
            preserve_default=False,
        ),
    ]