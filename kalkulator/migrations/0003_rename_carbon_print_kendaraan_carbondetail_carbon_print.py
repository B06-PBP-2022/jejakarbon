# Generated by Django 4.1 on 2022-10-27 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0002_komponenkalkulator_tagihan_listrik_rupiah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbondetail',
            old_name='carbon_print_kendaraan',
            new_name='carbon_print',
        ),
    ]