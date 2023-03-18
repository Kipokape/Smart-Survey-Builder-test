# Generated by Django 4.1.7 on 2023-03-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='IQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.CharField(max_length=300, verbose_name='Текст вопроса')),
                ('one_answer_with_a_choice', models.BooleanField(default=True, null=True, verbose_name='Выбор только 1 ответа')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'i_question',
            },
        ),
        migrations.CreateModel(
            name='ITestQuestion',
            fields=[
                ('iquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question_blocks.iquestion')),
            ],
            options={
                'db_table': 'i_test_question',
            },
            bases=('question_blocks.iquestion', models.Model),
        ),
        migrations.CreateModel(
            name='QuestionSimple',
            fields=[
                ('iquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='question_blocks.iquestion')),
                ('position_survey', models.IntegerField(default=None, null=True, verbose_name='Позиция в списке вопросов')),
            ],
            options={
                'db_table': 'question_simple',
            },
            bases=('question_blocks.iquestion', models.Model),
        ),
    ]
