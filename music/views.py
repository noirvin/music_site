from .models import Musician, Album, Song
from django.shortcuts import render

def home(request):
    artist_list = {
    'musicians': Musician.objects.all()
  }
    return render(request, 'home.html', artist_list)



def artist(request,musician_id):
    album_list = {
        'musician': Musician.objects.get(id=musician_id),
        'albums': Album.objects.filter(id=musician_id),
  }
    return render(request, 'artist.html', album_list)

def album(request,album_id):
    song_list = {
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album=album_id)

    }
    return render(request, 'album.html', song_list)
def song(request, song_id):
  one_song = {
    'song': Song.objects.get(id=song_id),
  }
  return render(request, 'song.html', one_song)
