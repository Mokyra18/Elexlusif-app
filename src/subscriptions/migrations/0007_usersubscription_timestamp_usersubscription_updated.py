# Generated by Django 5.0.7 on 2024-07-16 15:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_usersubscription_cancel_at_period_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubscription',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
