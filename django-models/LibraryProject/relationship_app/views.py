from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Vue basée sur les fonctions pour lister les livres
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Vue basée sur les classes pour afficher les détails d'une bibliothèque
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'Library'
