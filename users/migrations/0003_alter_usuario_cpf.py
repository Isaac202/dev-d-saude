# Generated by Django 3.2.9 on 2021-11-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211117_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(default=1, max_length=18, unique=True),
            preserve_default=False,
        ),
    ]