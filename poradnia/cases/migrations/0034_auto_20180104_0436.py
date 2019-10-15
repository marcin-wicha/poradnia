
# Generated by Django 1.11.8 on 2018-01-04 03:36
from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0033_auto_20170929_0815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case',
            options={'ordering': ['last_send'], 'permissions': (('can_view', 'Can view'), ('can_assign', 'Can assign new permissions'), ('can_send_to_client', 'Can send text to client'), ('can_manage_permission', 'Can assign permission'), ('can_add_record', 'Can add record'), ('can_change_own_record', 'Can change own records'), ('can_change_all_record', 'Can change all records'), ('can_close_case', 'Can close case'), ('can_select_client', 'Can select client')), 'verbose_name': 'Case', 'verbose_name_plural': 'Cases'},
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='0', max_length=100, no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status'),
        ),
    ]
