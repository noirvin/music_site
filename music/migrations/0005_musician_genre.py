# Generated by Django 3.0.4 on 2020-05-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='genre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
