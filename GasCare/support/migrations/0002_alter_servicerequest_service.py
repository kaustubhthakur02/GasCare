# Generated by Django 5.0.4 on 2024-04-25 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service',
            field=models.CharField(choices=[('Gas Booking', 'Gas Booking'), ('New Connection', 'New Connection'), ('Customer Support', 'Customer Support')], max_length=100),
        ),
    ]