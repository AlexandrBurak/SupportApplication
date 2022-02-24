# Generated by Django 2.2.16 on 2022-02-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_ticket_supporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Close', 'Close'), ('Freeze', 'Freeze')], default='Open', max_length=50),
        ),
    ]
