
# Generated by Django 1.11.13 on 2019-04-04 01:37
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advicer', '0016_auto_20190404_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Subject'),
        ),
    ]
