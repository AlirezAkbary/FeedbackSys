# Generated by Django 3.0.2 on 2020-02-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0005_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.TextField(default='Your Answer'),
        ),
    ]
