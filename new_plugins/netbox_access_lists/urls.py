# urls.py
from django.urls import path
from .views import (
    SpliceTrayListView, SpliceTrayCreateView, SpliceTrayUpdateView, SpliceTrayDeleteView,
    CouplerListView, CouplerCreateView, CouplerUpdateView, CouplerDeleteView
)

app_name = 'netbox_access_lists'

urlpatterns = [
    path('splice-tray/', SpliceTrayListView.as_view(), name='splice_tray_list'),


    path('coupler/', CouplerListView.as_view(), name='coupler'),


]
