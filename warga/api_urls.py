from django.urls import path
from . import api_views # Impor dari api_views.py yang baru kita buat

urlpatterns = [
    # URL untuk: /api/pengaduan/
    path('warga/', api_views.WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', api_views.WargaDetailAPIView.as_view(), name='api-warga-detail'),
    # GET -> List, POST -> Create
    path('pengaduan/', api_views.PengaduanListCreateAPIView.as_view(), name='api-pengaduan-list'),

    # URL untuk: /api/pengaduan/1/, /api/pengaduan/2/, dst.
    # GET -> Detail, PUT/PATCH -> Update, DELETE -> Hapus
    path('pengaduan/<int:pk>/', api_views.PengaduanDetailAPIView.as_view(), name='api-pengaduan-detail'),
]