# Generated by Django 4.0.4 on 2022-05-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prop', '0002_contectform_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=150)),
                ('phone', models.TextField(max_length=10)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
        migrations.DeleteModel(
            name='ContectForm',
        ),
    ]
