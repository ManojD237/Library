from django.shortcuts import render, redirect, get_object_or_404
from .models import Library
from .forms import LibraryForm

def home(request):
    return render(request, 'home.html')

# Library Views
def library_list(request):
    records = Library.objects.all()
    return render(request, 'library_list.html', {'records': records})

def library_upload(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'library_form.html', {'form': form})

def library_update(request, pk):
    record = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm(instance=record)
    return render(request, 'library_form.html', {'form': form})

def library_delete(request, pk):
    record = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('library_list')
    return render(request, 'library_confirm_delete.html', {'record': record})


