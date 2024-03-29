# Generated by Django 4.0.2 on 2022-02-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_profile_email_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='URI',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issuecomment',
            name='comment',
            field=models.TextField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='issueseverity',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issuestatus',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issuetype',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_github',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
