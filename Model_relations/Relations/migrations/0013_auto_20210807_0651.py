# Generated by Django 2.2.24 on 2021-08-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Relations', '0012_auto_20210807_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aricle',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Relations.Reporter'),
        ),
    ]