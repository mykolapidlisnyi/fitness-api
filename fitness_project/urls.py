from django.contrib import admin
from django.urls import path, include # Обов'язково додай include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), # Цей рядок спрямує запити до нашого додатку
]