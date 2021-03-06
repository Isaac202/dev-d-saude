# Generated by Django 3.2.9 on 2021-11-17 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('data_created', models.DateField(auto_now_add=True)),
                ('criado_por', models.CharField(blank=True, max_length=25, null=True)),
                ('proficional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='servicos.sercico')),
            ],
        ),
    ]
