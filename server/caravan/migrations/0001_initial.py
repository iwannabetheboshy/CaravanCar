# Generated by Django 4.1.1 on 2022-09-25 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=50)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
