# Generated by Django 2.2.2 on 2019-07-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20190701_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(),
        ),
    ]