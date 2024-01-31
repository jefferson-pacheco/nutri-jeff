# Generated by Django 5.0 on 2024-01-08 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('percentual_gordura', models.IntegerField()),
                ('percentual_musculo', models.IntegerField()),
                ('colesterol_hdl', models.IntegerField()),
                ('colesterol_ldl', models.IntegerField()),
                ('coleterol_totl', models.IntegerField()),
                ('trigliceridios', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.pacientes')),
            ],
        ),
    ]
