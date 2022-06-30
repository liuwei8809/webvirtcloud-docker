# Generated by Django 3.2.12 on 2022-06-29 12:13

from django.db import migrations
from django.utils.translation import gettext_lazy as _


def add_default_settings(apps, schema_editor):
    setting = apps.get_model("appsettings", "AppSettings")
    db_alias = schema_editor.connection.alias
    setting.objects.using(db_alias).bulk_create([
        setting(31, _("VM DRBD Status"), "VM_DRBD_STATUS", "False", "True,False", _("Show VM DRBD Status")),
    ])


def del_default_settings(apps, schema_editor):
    setting = apps.get_model("appsettings", "AppSettings")
    db_alias = schema_editor.connection.alias
    setting.objects.using(db_alias).filter(key="VM_DRBD_STATUS").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('appsettings', '0006_alter_appsettings_id'),
    ]

    operations = [
	    migrations.RunPython(add_default_settings, del_default_settings),
    ]
