# Generated by Django 3.1.3 on 2020-12-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bioblog', '0005_auto_20201203_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
