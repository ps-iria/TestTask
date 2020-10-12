from django.urls import path

from deals.views import DealUpload

urlpatterns = [
    path('api/users-csv-export/', DealUpload.as_view())
    ]
