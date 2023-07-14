from django.contrib import admin
from django.urls import path

from pdf.views import GeneratePdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pdf/',GeneratePdf.as_view(), name='PDF'),
]
