# Generated by Django 2.1.2 on 2019-09-28 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0020_auto_20190917_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
