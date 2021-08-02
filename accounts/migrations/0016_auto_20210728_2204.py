# Generated by Django 3.0.6 on 2021-07-28 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210728_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gainlosschartdata',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 422045), null=True),
        ),
        migrations.AlterField(
            model_name='gainlosshistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 421453), null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 418865), null=True),
        ),
        migrations.AlterField(
            model_name='totalgainloss',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 420842), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 417846), null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 28, 22, 4, 30, 420420), null=True),
        ),
    ]
