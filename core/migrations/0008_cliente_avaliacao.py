# Generated by Django 4.1.1 on 2022-10-01 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='avaliacao',
            field=models.CharField(default=1, max_length=10, verbose_name='Avaliacao'),
            preserve_default=False,
        ),
    ]
