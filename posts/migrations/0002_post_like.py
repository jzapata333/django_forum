# Generated by Django 3.2.6 on 2021-09-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveBigIntegerField(default=0, verbose_name='like'),
        ),
    ]
