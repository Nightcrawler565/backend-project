# Generated by Django 4.2.9 on 2024-02-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_alter_loandata_interest_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]