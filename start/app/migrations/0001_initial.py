# Generated by Django 2.1.7 on 2019-04-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='タスク')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='登録時間')),
            ],
        ),
    ]
