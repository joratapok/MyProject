from django.urls import path

from MyApp import views

urlpatterns = [
    path('', views.CommentsView.as_view(), name='comment_list'),
    path('fish', views.FishView.as_view(), name='fish'),
    path('links', views.LinksView.as_view(), name='links'),
    path('add_comment', views.AddCommentView.as_view(), name='add_comment'),
]