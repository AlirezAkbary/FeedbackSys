# Generated by Django 2.2.5 on 2020-02-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0007_auto_20200202_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Status',
            field=models.CharField(choices=[('active', 'active'), ('archived', 'archived')], default='active', max_length=20, null=True),
        ),
    ]