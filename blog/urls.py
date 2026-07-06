from django.urls import path

from .views import (
    PostListCreateAPIView,
    PostRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "posts/",
        PostListCreateAPIView.as_view(),
        name="post-list",
    ),
   path(
    "posts/<uuid:pk>/",
    PostRetrieveUpdateDestroyAPIView.as_view(),
    name="post-detail",
)
]