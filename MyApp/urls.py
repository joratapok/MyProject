from django.urls import path

from MyApp import views

urlpatterns = [
    path('', views.CommentsView.as_view(), name='comment_list'),
    path('fish', views.FishView.as_view(), name='fish'),
    path('add_comment', views.AddCommentView.as_view(), name='add_comment'),
    #path('profile', views.CommentsView.as_view(), name='profile'),
]