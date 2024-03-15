# Generated by Django 5.0.3 on 2024-03-15 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdmin', '0012_rename_stdsem_id_subject_stdsem_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_ids', models.CharField(max_length=50)),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_gender', models.CharField(max_length=50)),
                ('teacher_birthdate', models.DateField()),
                ('teacher_joindate', models.DateField()),
                ('teacher_qualification', models.CharField(max_length=100)),
                ('teacher_experience', models.CharField(max_length=100)),
                ('teacher_address', models.TextField()),
                ('teacher_mobile', models.CharField(max_length=30)),
                ('teacher_status', models.IntegerField(default=1)),
            ],
        ),
    ]
