from rest_framework import serializers
from .models import Pengaduan, Warga # Ambil model yang ada

# Serializer ini akan mengubah data Model 'Pengaduan' menjadi JSON
# Ini sangat mirip dengan cara kerja ModelForm Anda
class PengaduanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pengaduan

        # Tentukan field mana yang ingin Anda ekspos di API
        # 'pelapor' akan diekspos sebagai ID (Primary Key) dari Warga
        fields = ['id', 'judul', 'deskripsi', 'status', 'tanggal_lapor', 'pelapor']

        # Set field 'tanggal_lapor' sebagai read-only
        # karena field ini diisi otomatis oleh model (auto_now_add=True)
        read_only_fields = ['tanggal_lapor']