# Generated by Django 4.1.1 on 2022-09-25 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caravan', '0003_alter_post_wheel_alter_post_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='wheel',
            field=models.CharField(choices=[('4WD', '4WD'), ('RWD', 'RWD'), ('FWD', 'FWD')], default='', max_length=5),
        ),
    ]
