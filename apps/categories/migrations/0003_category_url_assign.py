# Generated by Django 4.0 on 2022-02-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url_assign',
            field=models.CharField(default='tmp', max_length=64),
            preserve_default=False,
        ),
    ]