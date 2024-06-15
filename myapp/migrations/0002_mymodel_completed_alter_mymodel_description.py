# Generated by Django 4.2.13 on 2024-06-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]