from django.urls import path
from .views import ClassicRestauListView, ClassicRestauDetailView, ClassicRestauUpdateView, ClassicRestauDeleteView, ClassicRestauCreateView

urlpatterns = [
    path('', ClassicRestauListView.as_view(), name='restau_list'),
    path('<int:pk>/', ClassicRestauDetailView.as_view(), name='restau_detail'),
    path('<int:pk>/update/', ClassicRestauUpdateView.as_view(), name='restau_update'),
    path('<int:pk>/delete/', ClassicRestauDeleteView.as_view(), name='restau_delete'),
    path('create/', ClassicRestauCreateView.as_view(), name='restau_create'),
]
