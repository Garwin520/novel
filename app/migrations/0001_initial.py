# Generated by Django 2.1.3 on 2020-05-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('belong', models.CharField(max_length=10)),
                ('chapter_url', models.CharField(max_length=100)),
                ('chapter_num', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Novels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('resume', models.CharField(max_length=200)),
                ('images_url', models.CharField(max_length=100)),
            ],
        ),
    ]
