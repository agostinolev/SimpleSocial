from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url('',views.PostList.as_view(),name='all'),
    url('new/',views.CreatePost.as_view(),name='create'),
    url(r'by/<username>/',views.UserPosts.as_view(),name='for_user'),
    url(r'by/<username>/<int:pk>/',views.PostDetail.as_view(),name='single'),
    url(r'delete/<int:pk>/',views.DeletePost.as_view(),name='delete')
]
