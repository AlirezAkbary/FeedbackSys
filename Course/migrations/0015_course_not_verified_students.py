# Generated by Django 2.0.7 on 2020-02-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
        ('Course', '0014_auto_20200206_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='not_verified_students',
            field=models.ManyToManyField(related_name='not_verified', to='Student.Student'),
        ),
    ]
