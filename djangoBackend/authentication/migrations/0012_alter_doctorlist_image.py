# Generated by Django 5.0.2 on 2024-03-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_doctorlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorlist',
            name='image',
            field=models.ImageField(blank=True, upload_to='docImages'),
        ),
    ]
