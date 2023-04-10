# Generated by Django 4.2 on 2023-04-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proekti', '0005_alter_doppolenaproekte_dop_pole_proekta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resheniepoproektu',
            name='status_ispolnenia',
        ),
        migrations.AddField(
            model_name='proekt',
            name='status_ispolnenia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proekti.statusispolnenia', verbose_name='Статус исполения решения'),
        ),
    ]