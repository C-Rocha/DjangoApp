# Generated by Django 4.1.1 on 2022-10-01 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='features',
            old_name='imagem',
            new_name='icone',
        ),
    ]
