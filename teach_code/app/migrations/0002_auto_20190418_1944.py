# Generated by Django 2.1.7 on 2019-04-18 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codemodel',
            options={'ordering': ('-date',)},
        ),
    ]
