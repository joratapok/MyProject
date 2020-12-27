from django.urls import path

from MyApp import views

urlpatterns = [
    path('', views.CommentsView.as_view(), name='comment_list'),
    path('add_comment', views.AddCommentView.as_view(), name='add_comment'),
]