# Generated by Django 4.0.2 on 2022-04-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_issuetype_color_issuewithtitles_iscomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuewithtitles',
            name='issueSeverity',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='issuewithtitles',
            name='issueStatus',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='issuewithtitles',
            name='issueType',
            field=models.JSONField(),
        ),
    ]
