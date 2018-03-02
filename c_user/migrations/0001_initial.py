# Generated by Django 2.0.1 on 2018-01-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('reciver', models.CharField(help_text='收件人', max_length=20)),
                ('sheng', models.CharField(default='', max_length=8)),
                ('shi', models.CharField(default='', max_length=16)),
                ('qu', models.CharField(default='', max_length=16)),
                ('detialaddr', models.CharField(default='', max_length=100)),
                ('rphone', models.CharField(default='', max_length=11)),
                ('yzbm', models.CharField(default='0', max_length=6)),
                ('mrdz', models.BooleanField(default='0', max_length=1)),
                ('scbz', models.BooleanField(default='0', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemil', models.EmailField(max_length=30)),
                ('urelname', models.CharField(default='', max_length=20)),
                ('uadr', models.CharField(default='', max_length=100)),
                ('uphone', models.CharField(default='', max_length=11)),
                ('usex', models.CharField(default='0', max_length=1)),
            ],
        ),
    ]