# Generated by Django 4.2.1 on 2023-06-23 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rareuser',
            name='profile_image_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='ended_on',
            field=models.DateField(null=True),
        ),
    ]
