# Generated by Django 2.0.7 on 2020-02-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0013_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Questions',
            field=models.ManyToManyField(blank=True, to='Question.Question'),
        ),
    ]