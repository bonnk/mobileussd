# Generated by Django 3.2.9 on 2021-12-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0003_auto_20211215_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankaccount',
            old_name='serviceCode',
            new_name='bankCode',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='sessiondId',
            new_name='customerId',
        ),
        migrations.RenameField(
            model_name='bankdetails',
            old_name='sessiondId',
            new_name='customerId',
        ),
    ]