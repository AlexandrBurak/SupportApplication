# Generated by Django 2.2.16 on 2022-02-24 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20220224_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='supporter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.Support'),
        ),
    ]
