# Generated by Django 5.0.4 on 2024-04-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_alter_servicerequest_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Resolved', 'Resolved'), ('In Progress', 'In Progress')], default='in_progress', max_length=20),
        ),
    ]
