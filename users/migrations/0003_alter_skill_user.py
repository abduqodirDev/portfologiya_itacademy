# Generated by Django 4.2.7 on 2024-02-09 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_skill', to='users.profile'),
        ),
    ]
