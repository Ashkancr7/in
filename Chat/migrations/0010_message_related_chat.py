# Generated by Django 3.1.1 on 2020-11-22 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0009_remove_message_related_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='related_chat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Chat.chat'),
        ),
    ]
