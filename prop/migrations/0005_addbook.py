# Generated by Django 4.0.4 on 2022-05-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prop', '0004_rename_contect_contect_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
