# Generated by Django 2.2.4 on 2019-09-03 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Level_Up_App', '0014_personalityanswer_personalityquestion_personalityquestionaire1_personalityquestionaire2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalityAnswerPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalityAnswerPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='PersonalityAnswer',
        ),
        migrations.AddField(
            model_name='personalityanswerpair',
            name='answer',
            field=models.ManyToManyField(to='Level_Up_App.PersonalityAnswerPosition'),
        ),
        migrations.AddField(
            model_name='personalityanswerpair',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Level_Up_App.PersonalityQuestion'),
        ),
    ]
