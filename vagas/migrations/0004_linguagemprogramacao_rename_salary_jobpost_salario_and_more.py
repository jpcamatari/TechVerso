# Generated by Django 5.1.7 on 2025-04-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_jobpost_contract_type_jobpost_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinguagemProgramacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='jobpost',
            old_name='salary',
            new_name='salario',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='contract_type',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='description',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='location',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='posted_date',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='title',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='beneficios',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='carga_horaria',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='cidade',
            field=models.CharField(default='São Paulo', max_length=255),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='data_publicacao',
            field=models.DateField(default='2025-01-01'),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='idioma_necessario',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='informacoes_empresa',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='link_inscricao',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='local_trabalho',
            field=models.CharField(blank=True, choices=[('Presencial', 'Presencial'), ('Híbrido', 'Híbrido'), ('Remoto', 'Remoto')], default='Remoto', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='oportunidades_crescimento',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='prazo_inscricao',
            field=models.DateField(blank=True, default='2025-01-01', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='requisitos',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='responsabilidades',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='tecnologias_usadas',
            field=models.CharField(blank=True, choices=[('Backend', 'Backend'), ('Frontend', 'Frontend'), ('Full Stack', 'Full Stack')], default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='tipo_contrato',
            field=models.CharField(choices=[('CLT', 'CLT'), ('PJ', 'PJ'), ('Estágio', 'Estágio'), ('Freelancer', 'Freelancer')], default='CLT', max_length=100),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='titulo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='linguagens_programacao',
            field=models.ManyToManyField(blank=True, to='vagas.linguagemprogramacao'),
        ),
    ]
