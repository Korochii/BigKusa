# Generated by Django 3.2.3 on 2021-06-14 23:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_entry_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added'),
        ),
    ]
