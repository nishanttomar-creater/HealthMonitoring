# Generated by Django 5.0.2 on 2024-03-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_appointments_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorlist',
            name='image',
            field=models.ImageField(default=None, upload_to='docImages'),
        ),
    ]
