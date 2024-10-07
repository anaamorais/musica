from django import forms
from .models import Playlist, Musica

class PlaylistForm(forms.ModelForm):
    class meta:
        model = Playlist
        fields = '__all__'

class MusicaForm(forms.ModelForm):
    class meta:
        model = Musica
        fields = '__all__'