# Generated by Django 4.1.6 on 2023-12-02 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convenios', '0005_remove_convenio_participantes_alter_convenio_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='numero',
            field=models.CharField(max_length=10),
        ),
    ]
