# Generated by Django 4.0.2 on 2022-04-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_project_admin_project_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to='main.Profile'),
        ),
    ]
