# Generated by Django 5.1.4 on 2025-06-20 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0003_participant_is_winner_alter_participant_token_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='token_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
