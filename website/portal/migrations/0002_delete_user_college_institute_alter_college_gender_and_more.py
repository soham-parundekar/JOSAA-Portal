# Generated by Django 4.2.2 on 2023-07-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='college',
            name='institute',
            field=models.CharField(default='NaN', max_length=200),
        ),
        migrations.AlterField(
            model_name='college',
            name='gender',
            field=models.CharField(default='NaN', max_length=50),
        ),
        migrations.AlterField(
            model_name='college',
            name='program_name',
            field=models.CharField(default='NaN', max_length=200),
        ),
        migrations.AlterField(
            model_name='college',
            name='quota',
            field=models.CharField(default='NaN', max_length=50),
        ),
    ]
