# Generated by Django 3.2.6 on 2021-08-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_alter_studentmanagement_roll_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmanagement',
            name='roll_no',
            field=models.IntegerField(),
        ),
    ]
