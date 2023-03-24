# Generated by Django 4.1.7 on 2023-03-24 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('survey_base', '0001_initial'),
        ('answer_blocks', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IResultAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='answer_blocks.ianswer', verbose_name='Структура ответа')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'i_result_answer',
            },
        ),
        migrations.CreateModel(
            name='ResultSelect',
            fields=[
                ('iresultanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey_passing.iresultanswer')),
            ],
            options={
                'db_table': 'result_select',
            },
            bases=('survey_passing.iresultanswer', models.Model),
        ),
        migrations.CreateModel(
            name='ResultTextInput',
            fields=[
                ('iresultanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='survey_passing.iresultanswer')),
                ('input_text', models.CharField(max_length=300, verbose_name='Введённый текст')),
            ],
            options={
                'db_table': 'result_test_input',
            },
            bases=('survey_passing.iresultanswer', models.Model),
        ),
        migrations.CreateModel(
            name='TakingSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_end', models.DateTimeField(auto_now_add=True, verbose_name='Был пройден')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_base.isurvey', verbose_name='Проходимый опрос')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Проходящий')),
            ],
            options={
                'db_table': 'taking_survey',
            },
        ),
        migrations.AddField(
            model_name='iresultanswer',
            name='taking_survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_passing.takingsurvey', verbose_name='Прохождение'),
        ),
    ]
