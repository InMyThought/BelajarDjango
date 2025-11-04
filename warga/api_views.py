from rest_framework import generics
from .models import Pengaduan
from .serializers import PengaduanSerializer

# View ini menangani dua hal:
# 1. GET: Mendapatkan DAFTAR semua pengaduan (List)
# 2. POST: Membuat pengaduan BARU (Create)
# Ini sesuai dengan metode HTTP 'GET' dan 'POST'
class PengaduanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer

# View ini menangani tiga hal untuk SATU item spesifik (berdasarkan 'pk'):
# 1. GET: Mendapatkan DETAIL satu pengaduan (Retrieve)
# 2. PUT/PATCH: Memperbarui satu pengaduan (Update)
# 3. DELETE: Menghapus satu pengaduan (Destroy)
# Ini sesuai dengan metode HTTP 'GET', 'PUT', 'PATCH', dan 'DELETE'
class PengaduanDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pengaduan.objects.all()
    serializer_class = PengaduanSerializer