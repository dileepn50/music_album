from django import shortcuts
from django import http
from django.views import generic
from django.views.generic import edit


from music import models

# Create your views here.
'''
def index(request):
    all_albums = models.Album.objects.all()

    args = {'all_albums': all_albums}
    return shortcuts.render(request, 'music/index.html', args)


def detail(request, album_id):
    album = shortcuts.get_object_or_404(models.Album, pk=album_id)
    args = {'album': album}
    return shortcuts.render(request, 'music/detail.html', args)
'''

class ListView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return models.Album.objects.all()

class DetailView(generic.DetailView):
    model = models.Album
    template_name = 'music/detail.html'

class CreateView(edit.CreateView):
    model = models.Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


def favourite(request, album_id):
    #print(request.POST)
    song_id = request.POST['song']
    album = shortcuts.get_object_or_404(models.Album,pk=album_id)
    song = album.song_set.get(pk=int(song_id))
    song.is_favorite = True
    song.save()
    args = {'album': album}
    return shortcuts.render(request, 'music/detail.html', args)
