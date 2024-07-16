# Generated by Django 5.0.7 on 2024-07-16 12:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscriptionprice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['order', 'featured', '-updated'], 'permissions': [('advanced', 'Advanced Perm'), ('pro', 'Pro Perm'), ('basic', 'Basic Perm'), ('basic_ai', 'Basic AI Perm')]},
        ),
        migrations.AddField(
            model_name='subscription',
            name='featured',
            field=models.BooleanField(default=True, help_text='Featured on Django pricing page'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='features',
            field=models.TextField(blank=True, help_text='Features for pricing, seperated by new line', null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='order',
            field=models.IntegerField(default=-1, help_text='Ordering on Django pricing page'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
