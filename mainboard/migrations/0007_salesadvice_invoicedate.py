# Generated by Django 2.0 on 2017-12-07 05:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0006_auto_20171207_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesadvice',
            name='invoiceDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
