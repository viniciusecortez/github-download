from django.urls import path
from main_app.views import index as main_index, download as main_download
urlpatterns = [
    path('', main_index),
    path('download/<str:file>', main_download)
]
