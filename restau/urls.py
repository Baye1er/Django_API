from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestauListAPIView.as_view(), name='restau_list'),
    path('<int:id>/', views.RestauRetrieveAPIView.as_view(), name='restau_detail'),
    path('create/', views.RestauCreateAPIView.as_view(), name='restau_create'),
    path('update/<int:id>/', views.RestauRetrieveUpdateAPIView.as_view(), name='restau_update'),
    path('delete/<int:id>/', views.RestauDestroyAPIView.as_view(), name='restau_delete'),
]