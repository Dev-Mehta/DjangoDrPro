# Generated by Django 3.0.3 on 2020-08-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20200812_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previousreport',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3),
        ),
    ]