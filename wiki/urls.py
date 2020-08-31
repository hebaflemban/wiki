
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fakewiki/topics/', views.list, name = 'page-list'),
    path('fakewiki/<int:page_id>', views.detail, name ='page-detail' ),
]
