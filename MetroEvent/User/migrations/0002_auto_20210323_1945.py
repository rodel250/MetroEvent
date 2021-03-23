# Generated by Django 2.1.15 on 2021-03-23 11:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('organizerID', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Organizer',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 23, 19, 45, 19, 334177), null=True),
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='organizerUser', to='User.User'),
        ),
    ]
