# Generated by Django 3.0.2 on 2020-02-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0013_auto_20200207_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
    ]
