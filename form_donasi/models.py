from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OpenDonasi(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True ) # on_delete = jika User hilang, semua task juga hilang; #null=True => database boleh empty field
    tema_kegiatan = models.CharField(max_length=100)
    tanggal_pembuatan = models.DateTimeField(auto_now_add=True)
    deskripsi = models.TextField(null=True, blank=True)
    total_donasi_terkumpul = models.IntegerField(null=True, blank=True)
    target_donasi = models.PositiveIntegerField(default=0, blank=True)
   
    def __str__(self):
        return self.tema_kegiatan


   