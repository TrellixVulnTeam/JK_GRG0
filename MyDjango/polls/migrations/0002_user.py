# Generated by Django 2.2.3 on 2019-07-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickName', models.CharField(max_length=20, unique=True)),
                ('phoneNumber', models.ImageField(max_length=11, upload_to='')),
                ('sex', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
