# Generated by Django 2.1.5 on 2020-02-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0002_professor_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='VerifyCode',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
