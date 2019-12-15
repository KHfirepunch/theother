# Generated by Django 2.2.4 on 2019-12-15 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='태그명')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': '태그',
                'verbose_name_plural': '태그',
            },
        ),
    ]
