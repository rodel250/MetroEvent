# Generated by Django 2.1.15 on 2021-03-25 17:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20210324_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notificationID', models.AutoField(primary_key=True, serialize=False)),
                ('notificationDate', models.DateField(blank=True, default=datetime.datetime(2021, 3, 26, 1, 56, 7, 33789), null=True)),
                ('notificationSubject', models.CharField(blank=True, max_length=50, null=True)),
                ('notificationContent', models.CharField(blank=True, max_length=250, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificationEvent', to='User.Event')),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 26, 1, 56, 7, 31795), null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='notificationUser', to='User.User'),
        ),
    ]
