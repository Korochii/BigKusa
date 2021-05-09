# Generated by Django 2.2.12 on 2021-05-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAdded', models.DateTimeField()),
                ('text', models.TextField()),
                ('translation', models.TextField()),
                ('remarks', models.TextField()),
            ],
        ),
    ]
