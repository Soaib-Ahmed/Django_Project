# Generated by Django 5.0 on 2024-01-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_balance_after_transaction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('deposit', 'Deposit'), ('borrow', 'Borrow'), ('return', 'Return')], max_length=20),
        ),
    ]