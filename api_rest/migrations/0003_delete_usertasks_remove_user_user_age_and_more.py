# Generated by Django 5.1 on 2024-08-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_usertasks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserTasks',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='', max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
