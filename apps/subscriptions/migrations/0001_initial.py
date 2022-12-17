# Generated by Django 3.2.15 on 2022-12-17 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanSSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='subscription')),
            ],
            options={
                'db_table': 'plans_subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypesOfSubscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'types_subscriptions',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionsForUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_applied', models.FloatField(blank=True, default=0.0, null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions.planssubscriptions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'db_table': 'subscriptions_for_users',
            },
        ),
        migrations.AddField(
            model_name='planssubscriptions',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions.typesofsubscriptions'),
        ),
    ]
