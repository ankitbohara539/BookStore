from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

def home(request):
    context = {}
    return render(request, 'myapp/base.html', context)
def landing(request):
    return render(request, 'myapp/landing.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp/book_confirm_delete.html', {'book': book})
