# Generated by Django 2.2.10 on 2020-11-16 06:56

from django.db import migrations, models
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20201116_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('one_choice', 'one_choice'), ('multiple_choice', 'multiple_choice'), ('free_text', 'free_text')], default=polls.models.QuestionTypes(1), max_length=64, verbose_name='Тип ответа на вопрос'),
        ),
    ]
