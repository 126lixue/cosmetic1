# Generated by Django 2.0.1 on 2018-02-02 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_goods', '0004_typeinfo_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gpic',
            field=models.ImageField(upload_to='c_goods'),
        ),
    ]
