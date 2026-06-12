from django.urls import path
from . import views 

app_name = "blog"

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    # path('posts/create/', views, name='posts-create'),

    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='posts-detail'),
                # slug:<slug>/
    # path('posts/slug:<slug>/edit/', views, name='posts-edit'),
    # path('posts/slug:<slug>/delete/', views, name='posts-delete'),

    ]
