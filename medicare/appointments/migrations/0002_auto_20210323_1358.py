# Generated by Django 3.1.1 on 2021-03-23 20:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(choices=[(datetime.datetime(2021, 3, 23, 8, 0), datetime.datetime(2021, 3, 23, 8, 0)), (datetime.datetime(2021, 3, 23, 10, 0), datetime.datetime(2021, 3, 23, 10, 0)), (datetime.datetime(2021, 3, 23, 12, 0), datetime.datetime(2021, 3, 23, 12, 0)), (datetime.datetime(2021, 3, 23, 14, 0), datetime.datetime(2021, 3, 23, 14, 0)), (datetime.datetime(2021, 3, 23, 16, 0), datetime.datetime(2021, 3, 23, 16, 0))]),
        ),
    ]
