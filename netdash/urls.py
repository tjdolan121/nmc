from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/detail_view/edit_status/', views.edit_status_view, name='edit_status'),
    path('<slug:slug>/detail_view/delete_favorite/<int:pk>/', views.delete_favorite_view, name='delete_favorite'),
    path('<slug:slug>/detail_view/delete_message/<int:pk>/', views.delete_message_view, name='delete_message'),
    path('<slug:slug>/detail_view/edit_service/<int:pk>/', views.edit_service_view, name='edit_service'),
    path('<slug:slug>/detail_view/', views.detail_view, name='detail_view'),
    path('<slug:slug>/add_favorite/', views.add_favorite_view, name='add_favorite'),
    path('<slug:slug>/add_service', views.add_service_view, name='add_service'),
    path('<slug:slug>/add_message/', views.add_message_view, name='add_message'),
    path('<slug:slug>/', views.netdash_view, name='netdash'),
    path('', views.home_view, name='home')
]
