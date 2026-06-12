from django.urls import path
from . import views 

app_name = "comment"

urlpatterns = [
    # see comment for a post
    path('post/<slug:slug>/', views.PostCommentListView.as_view(), ),
    
    # manage comments from admin
    path('admin/post/<slug:slug>/', views.AdminCommentListView.as_view(), ),
    path('admin/post/<slug:slug>/<int:pk>/manage/', views.AdminCommentRetrieveUpdateDestroyView.as_view(), )

]