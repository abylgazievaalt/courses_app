# Generated by Django 2.2.3 on 2019-07-02 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20190702_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(),
        ),
    ]