# Generated by Django 2.0.4 on 2018-04-10 10:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20180410_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2df8d5f9-5ebe-47c2-bc10-e0a3f99af6f9'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='path',
            field=models.CharField(default='ae4b279f', max_length=200),
        ),
    ]