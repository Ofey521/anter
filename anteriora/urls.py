from django.urls import path
from .views import (PostListView, PostDetailView ,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView)
from . import views

# z urla anteriora prowadzi tu
urlpatterns = [
    path('', PostListView.as_view(), name='anteriora-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name = 'post-detail'),# primaryKey czyli post nr 1,2,3
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='anteriora-about'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('ranking/', views.ranking, name='anteriora-ranking'),
    path('user/<username>', UserPostListView.as_view(), name='user-posts'),
    path('help/', views.help, name="anteriora-help"),

]

# konwencja templatek
# <app>/<model>_<viewtype>.html
# np anteriora/post_list_list.html
