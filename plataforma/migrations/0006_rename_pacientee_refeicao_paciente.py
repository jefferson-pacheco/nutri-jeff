# Generated by Django 5.0 on 2024-01-11 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0005_refeicao_opcao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refeicao',
            old_name='pacientee',
            new_name='paciente',
        ),
    ]
