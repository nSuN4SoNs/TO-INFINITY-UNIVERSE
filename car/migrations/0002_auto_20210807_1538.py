# Generated by Django 3.2.3 on 2021-08-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carcolor',
            options={'verbose_name_plural': 'Colors'},
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
