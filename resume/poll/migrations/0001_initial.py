# Generated by Django 3.2 on 2021-09-23 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_db', models.CharField(max_length=100, verbose_name='ФИО')),
                ('professional_db', models.CharField(max_length=100, verbose_name='Профессия')),
                ('sex_db', models.CharField(choices=[('Мужской', 'муж'), ('Женский', 'жен')], default='Мужской', max_length=10, verbose_name='Пол')),
                ('it_db', models.CharField(choices=[('Положительное', 'Положительно. За ним будущее.'), ('Нейтральное', 'Мне все равно. Будь как будет.'), ('Негативное', 'Я считаю что эти компуктеры погубят мир.')], default='Нейтральное', max_length=50, verbose_name='Отношение к IT')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]