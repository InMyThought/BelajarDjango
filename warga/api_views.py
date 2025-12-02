# Impor viewsets, bukan lagi generics
from rest_framework import viewsets 
from .models import Pengaduan, Warga
# Serializer Anda sudah siap
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .serializers import PengaduanSerializer, WargaSerializer 

# 1. PRAKTIKUM: ViewSet untuk Warga
# Class ini menggantikan WargaListAPIView dan WargaDetailAPIView
class WargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows 'warga' to be viewed or edited.
    Secara otomatis menyediakan aksi .list(), .retrieve(), .create(), 
    .update(), .partial_update(), dan .destroy()
    """
    # Ambil semua objek Warga, urutkan berdasarkan tanggal registrasi terbaru
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# 2. CHALLENGE: ViewSet untuk Pengaduan
# Class ini menggantikan PengaduanListCreateAPIView dan PengaduanDetailAPIView
class PengaduanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows 'pengaduan' to be viewed or edited.
    """
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer
    permission_classes = [IsAdminUser]