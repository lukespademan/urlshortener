# Generated by Django 2.0.5 on 2018-05-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0018_auto_20180529_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='id',
            field=models.UUIDField(default='2d3d9ed41f6e4d72b7fee3d34a2beeb2', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='link',
            name='path',
            field=models.CharField(default='65136ca9', max_length=200),
        ),
    ]