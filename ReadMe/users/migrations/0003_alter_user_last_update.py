# Generated by Django 4.2.7 on 2023-12-14 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]