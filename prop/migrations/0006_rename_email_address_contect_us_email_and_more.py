# Generated by Django 4.0.4 on 2022-05-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prop', '0005_addbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contect_us',
            old_name='email_address',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contect_us',
            old_name='message',
            new_name='msg',
        ),
        migrations.RenameField(
            model_name='contect_us',
            old_name='full_name',
            new_name='name',
        ),
    ]