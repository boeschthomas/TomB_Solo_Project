# Generated by Django 3.0.7 on 2020-06-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_bench_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
