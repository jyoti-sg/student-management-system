# Generated by Django 3.2.6 on 2021-08-25 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentmanagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('fees', models.CharField(max_length=50)),
                ('edit', models.CharField(max_length=50)),
                ('delete', models.CharField(max_length=50)),
            ],
        ),
    ]
