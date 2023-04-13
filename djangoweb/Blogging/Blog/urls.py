from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'Blog'

urlpatterns = [
    # path('', views.Post_List, name='Post_List'),
    path('', views.PostListView.as_view(), name='Post_List'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.Post_Detail, name='Post_Detail'),
    path('<int:post_id>/share/', views.Post_Share, name='Post_Share'),
    path('<int:post_id>/comment/', views.post_comment, name='Post_Comment'),
    path('tag/<slug:tag_slug>/', views.Post_List, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='Post_Feed'),
    path('search/', views.Post_search, name='Post_search')
    
    
    
    
    # path('', views.Draft_List, name='Draft_List'),
    # path('<int:id>/', views.Draft_post, name='Draft_post'),
]

