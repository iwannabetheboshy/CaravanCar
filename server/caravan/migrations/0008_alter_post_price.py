# Generated by Django 4.1.1 on 2022-09-25 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caravan', '0007_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(max_length=50),
        ),
    ]
