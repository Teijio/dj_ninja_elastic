# Generated by Django 5.1.4 on 2025-01-04 11:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='token',
            field=models.CharField(default=uuid.uuid4, max_length=255, verbose_name='User token'),
        ),
    ]
