# Generated by Django 2.2.2 on 2019-07-01 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20190701_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='snippets.Course'),
        ),
    ]