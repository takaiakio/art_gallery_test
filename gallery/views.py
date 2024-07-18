# gallery/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Art
from .forms import ArtForm

def art_list(request):
    arts = Art.objects.all()
    return render(request, 'gallery/art_list.html', {'arts': arts})

def upload_art(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('art_list')
    else:
        form = ArtForm()
    return render(request, 'gallery/upload_art.html', {'form': form})

def delete_art(request, pk):
    art = get_object_or_404(Art, pk=pk)
    if request.method == 'POST':
        art.delete()
        return redirect('art_list')
    return render(request, 'gallery/delete_art.html', {'art': art})
