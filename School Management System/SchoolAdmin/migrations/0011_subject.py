# Generated by Django 5.0.3 on 2024-03-13 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolAdmin', '0010_stdsem_stdsem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_status', models.IntegerField(default=1)),
                ('StdSem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolAdmin.stdsem')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolAdmin.department')),
            ],
        ),
    ]
