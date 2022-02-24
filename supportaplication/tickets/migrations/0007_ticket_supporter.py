# Generated by Django 2.2.16 on 2022-02-24 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_remove_ticket_supporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='supporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tickets', to='tickets.Support'),
        ),
    ]
