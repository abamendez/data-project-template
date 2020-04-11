# Generated by Django 3.0 on 2020-04-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=200)),
                ('registration_date', models.DateTimeField(verbose_name='date published')),
                ('vendor_eans', models.CharField(max_length=200)),
            ],
        ),
    ]
