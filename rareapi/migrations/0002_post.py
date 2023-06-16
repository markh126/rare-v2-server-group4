# Generated by Django 4.2.1 on 2023-06-14 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=40)),
                ('publication_date', models.DateField()),
                ('image_url', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
            ],
        ),
    ]
