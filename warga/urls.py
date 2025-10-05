from django.urls import path
from .views import WargaListView
from .views import WargaDetailView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),]