from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_comments, name="all_comments"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.CommentsDetailView.as_view(), name="detail_comment"),
    path('<int:pk>/delete', views.CommentsDeleteView.as_view(), name="comments_delete"),
    path('<int:pk>/update', views.CommentsUpdateView.as_view(), name="comments_update"),
    path('comment_view', views.CommentsListView.as_view(), name="comment_view")
]
