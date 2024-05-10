# Generated by Django 5.0.3 on 2024-05-06 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionRelate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_app.answer')),
                ('next_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_question', to='polls_app.question')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls_app.question')),
            ],
        ),
    ]
