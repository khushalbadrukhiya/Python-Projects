# Generated by Django 5.0.3 on 2024-03-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdmin', '0003_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_status',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_image',
            field=models.FileField(default='default_img.jpg', upload_to='media'),
        ),
    ]
