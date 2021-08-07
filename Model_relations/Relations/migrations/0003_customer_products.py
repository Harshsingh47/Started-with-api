# Generated by Django 2.2.24 on 2021-08-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relations', '0002_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.TextField(max_length=200)),
                ('cus_email', models.EmailField(max_length=254)),
                ('cus_mobile', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.TextField(max_length=20)),
                ('cus_qty', models.TextField(max_length=200)),
                ('cus_id', models.ManyToManyField(to='Relations.Customer')),
            ],
        ),
    ]