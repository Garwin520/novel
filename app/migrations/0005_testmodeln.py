# Generated by Django 2.1.3 on 2020-05-17 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_novels'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModeln',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]