# Generated by Django 2.2.10 on 2020-11-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20201112_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='name',
            field=models.CharField(default="(без имени)", max_length=256, verbose_name='Название опроса'),
            preserve_default=False,
        ),
    ]
