# Generated by Django 2.2.24 on 2021-08-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relations', '0018_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='working',
            name='address',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='working',
            name='name',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
