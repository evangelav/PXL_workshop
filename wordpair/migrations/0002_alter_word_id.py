# Generated by Django 4.1.6 on 2023-02-07 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordpair', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
