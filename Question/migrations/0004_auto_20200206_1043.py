# Generated by Django 2.1.5 on 2020-02-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0003_auto_20200203_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='q_type',
            field=models.CharField(choices=[('M', 'MultipleChoice'), ('L', 'LongAnswer')], default='M', max_length=1),
        ),
    ]
