# Generated by Django 3.1.7 on 2021-03-29 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20210329_1112'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sale',
            unique_together={('customer', 'book')},
        ),
    ]
