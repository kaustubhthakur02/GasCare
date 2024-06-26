# Generated by Django 5.0.4 on 2024-04-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('service', models.CharField(choices=[('gas_booking', 'Gas Booking'), ('new_connection', 'New Connection'), ('customer_support', 'Customer Support')], max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submission_datetime', models.DateTimeField(auto_now_add=True)),
                ('resolved_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('resolved', 'Resolved'), ('in_progress', 'In Progress')], default='in_progress', max_length=20)),
            ],
        ),
    ]
