# Generated by Django 3.0.2 on 2020-02-06 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0004_auto_20200206_1102'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SelectedChoices',
            field=models.ManyToManyField(blank=True, null=True, to='Question.Choice'),
        ),
    ]
