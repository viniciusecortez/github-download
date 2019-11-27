from django.urls import path
from main_app.views import index as main_index
urlpatterns = [
    path('', main_index),
]
