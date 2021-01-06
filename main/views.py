from django.shortcuts import render, redirect
from json import dumps
from .models import Note

def selector(request):
    if request.user.is_authenticated:
        many_notes = []
        for note in request.user.note_set.all():
            note = note.__dict__
            many_notes.append({key: note[key] for key in ['id', 'img', 'description', 'title']})
        context={'notes':dumps(many_notes)}
        return render(request, 'main/home.html', context)
    else:
        return redirect('accounts/login')

def add_note(request):
    title=request.POST.get('title')
    description = request.POST.get('description')
    img = request.POST.get('img')
    if len(title) or len(description) or len(img):
        request.user.note_set.create(title=title, description=description, img=img, author=request.user)
    return redirect('/')

def search(request):
    to_be_searched = request.POST['search']
    many_notes = [{'to_be_searched': to_be_searched}]
    for note in request.user.note_set.all():
        note = note.__dict__
        for key in ['description', 'title']:
            if note[key].find(to_be_searched)!=-1:
                many_notes.append({key1:note[key1] for key1 in ['id', 'description', 'title', 'img']})
                break
    context={'notes':dumps(many_notes)}
    return render(request, 'main/home.html', context)

def change(request):
    try:
        note_id = request.POST['id']
    except:
        return redirect('/')

    if not(request.POST.get('delete') is None):
        note = request.user.note_set.filter(id=note_id)
        note.delete()
        return redirect('/')
    else:
        note = Note.objects.filter(id=note_id).first().__dict__
        many_notes = [{key: note[key] for key in ['id', 'img', 'description', 'title']}]
        context = {'notes': note}
        return render(request, 'main/edit.html', context)

def edit(request):
    note_id = request.POST['id']
    note = request.user.note_set.filter(id=note_id)
    title=request.POST.get('title')
    description = request.POST.get('description')
    img = request.POST.get('img')
    if len(title) or len(description) or len(img):
        note = note.first()
        note.title = title
        note.description = description
        note.img = img
        note.save()
    else:
        note.delete()
    return redirect('/')

def about(request):
    return render(request, 'main/about.html')