# Generated by Django 4.1.5 on 2023-02-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_college_email_college_phone_college_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]