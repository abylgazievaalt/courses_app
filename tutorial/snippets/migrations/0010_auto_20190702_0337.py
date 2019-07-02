# Generated by Django 2.2.2 on 2019-07-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_contact_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.CharField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')], default='', max_length=10),
        ),
    ]