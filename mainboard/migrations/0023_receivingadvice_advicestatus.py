# Generated by Django 2.0 on 2017-12-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0022_auto_20171220_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='receivingadvice',
            name='adviceStatus',
            field=models.CharField(default='FOR APPROVAL', max_length=50),
        ),
    ]
