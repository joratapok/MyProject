from django.urls import path

from MyApp import views

urlpatterns = [
    path('', views.CommentsView.as_view(), name='comment_list'),
    path('fish', views.FishView.as_view(), name='fish'),
    path('js', views.JsView.as_view(), name='js'),
    path('links', views.LinksView.as_view(), name='links_list'),
    path('add_link', views.AddLinkView.as_view(), name='add_link'),
    path('add_comment', views.AddCommentView.as_view(), name='add_comment'),
    #path('profile', views.ProfileView.as_view(), name='profile'),
    path('update_profile', views.UpdateProfileView.as_view(), name='update_profile'),
]