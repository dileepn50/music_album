from django.conf.urls import url, include


from . import views


urlpatterns = [
    #'music/'
    url(r'^$', views.ListView.as_view(), name='index'),
    #'music/123'
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^favourite/(?P<album_id>[0-9]+)/$', views.favourite, name='favourite'),
    url(r'^album/add$', views.CreateView.as_view(), name='add-album'),

    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),



]
