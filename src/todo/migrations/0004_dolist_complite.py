# Generated by Django 2.2.1 on 2019-06-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190618_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='dolist',
            name='complite',
            field=models.BooleanField(default=False),
        ),
    ]