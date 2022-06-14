# from django.conf.urls import url
from django.urls import include, path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('$',views.index,name = 'index'),
    path('new/post$', views.new_post, name='new-post'),
    path('profile/(?P<user_id>\d+)?$', views.profile, name='profile'),
    path('update/profile$', views.updateprofile, name='updateprofile'),
    path('vote/(?P<post_id>\d+)?$', views.vote, name='vote'),    
    path('search/', views.search_results, name='search_results'),
    path('api/post/$', views.PostList.as_view()),
    path('api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
