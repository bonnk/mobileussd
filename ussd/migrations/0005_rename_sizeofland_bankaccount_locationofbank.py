# Generated by Django 3.2.9 on 2021-12-15 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0004_auto_20211215_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='sizeOfland',
            new_name='locationOfBank',
        ),
    ]
