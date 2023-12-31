from django.urls import path
from .views import BlogCreateView, BlogDetailView, BlogListView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name="home"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/detail/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")
]
