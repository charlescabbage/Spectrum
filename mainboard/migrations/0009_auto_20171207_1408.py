# Generated by Django 2.0 on 2017-12-07 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0008_salesadviceitems_itemqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesadvice',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mainboard.Store'),
        ),
    ]
