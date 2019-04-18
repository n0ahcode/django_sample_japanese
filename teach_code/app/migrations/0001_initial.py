# Generated by Django 2.1.7 on 2019-04-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='投稿時間')),
                ('title', models.CharField(max_length=128, verbose_name='タイトル')),
                ('text', models.TextField(max_length=1024, verbose_name='テキスト')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名前')),
            ],
        ),
        migrations.AddField(
            model_name='codemodel',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag', to='app.Tag'),
        ),
    ]
