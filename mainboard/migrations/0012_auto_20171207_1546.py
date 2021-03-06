# Generated by Django 2.0 on 2017-12-07 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainboard', '0011_auto_20171207_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportGeneratedDate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='salesadvice',
            name='invoiceNumber',
            field=models.CharField(default='ABC000000', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='salesreport',
            name='invoiceNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainboard.SalesAdvice'),
        ),
    ]
