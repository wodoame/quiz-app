# Generated by Django 4.2.5 on 2023-11-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_question_answer_question_instruction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='answer',
            field=models.CharField(max_length=128),
        ),
    ]