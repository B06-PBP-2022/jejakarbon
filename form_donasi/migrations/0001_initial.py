# Generated by Django 4.1 on 2022-11-01 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenDonasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema_kegiatan', models.CharField(max_length=100)),
                ('pencetus_donasi', models.CharField(max_length=100)),
                ('tanggal_pembuatan', models.DateTimeField(auto_now_add=True)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('total_donasi_terkumpul', models.IntegerField(blank=True, default=0)),
                ('target_donasi', models.PositiveIntegerField(blank=True, default=0)),
                ('username', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
