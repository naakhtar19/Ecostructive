# Generated by Django 3.0.6 on 2020-05-30 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('timeslot', models.CharField(max_length=200)),
            ],
        ),
    ]
