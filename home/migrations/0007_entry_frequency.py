# Generated by Django 3.2.3 on 2021-06-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_entry_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='frequency',
            field=models.IntegerField(default=1, verbose_name='Frequency'),
            preserve_default=False,
        ),
    ]
