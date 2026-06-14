from django.urls import path
from . import views

# app_name = "blog"

# urlpatterns = [
#     path('posts/', views.PostListView.as_view(), name='posts'),
#     path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='posts-detail'),

#     path('author/posts/<slug:slug>/', views.AuthorRUDView.as_view(), name='posts-detail-author'),
#     path('author/posts/create/', views.AuthorListCreateView.as_view(), name='posts-create-author'),
#     path('author/posts/', views.AuthorListCreateView.as_view(), name='posts-list-author'),
#     path('author/posts/slug:<slug>/edit/', views.AuthorRUDView.as_view(), name='posts-edit-author'),
#     path('author/posts/slug:<slug>/delete/', views.AuthorRUDView.as_view(), name='posts-delete-author'),

#     ]


from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # Public endpoints
    path("posts/", views.PostListView.as_view(), name="posts"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="posts-detail"),
    # Author endpoints
    path(
        "author/posts/",
        views.AuthorListCreateView.as_view(),
        name="author-posts-list-create",
    ),
    path(
        "author/posts/<slug:slug>/",
        views.AuthorRUDView.as_view(),
        name="author-posts-detail",
    ),
    path(
        "author/posts/<slug:slug>/edit/",
        views.AuthorRUDView.as_view(),
        name="author-posts-edit",
    ),
    path(
        "author/posts/<slug:slug>/delete/",
        views.AuthorRUDView.as_view(),
        name="author-posts-delete",
    ),
    # Category endpoints
    path("category/", views.CategoryView.as_view(), name="author-posts-delete"),
]
