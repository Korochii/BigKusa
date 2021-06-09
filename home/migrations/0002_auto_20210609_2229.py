# Generated by Django 3.2.3 on 2021-06-09 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='event_date',
        ),
        migrations.AddField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Added'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='owner',
            field=models.TextField(default='', verbose_name='Owner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='remarks',
            field=models.TextField(blank=True, verbose_name='Remarks'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='output_text',
            field=models.TextField(verbose_name='Translation'),
        ),
    ]
