# Generated by Django 4.1.5 on 2023-03-15 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_employee_aadhar_employee_fathername_employee_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='imageurl',
            field=models.CharField(max_length=100, null=True),
        ),
    ]