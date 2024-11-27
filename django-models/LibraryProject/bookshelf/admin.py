from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Affiche les champs dans la liste des livres
    list_display = ('title', 'author', 'publication_year')
    
    # Permet de rechercher des livres par titre et auteur dans l'admin
    search_fields = ('title', 'author')
    
    # Permet de filtrer les livres par année de publication
    list_filter = ('publication_year',)

    # Permet de rendre tous les champs modifiables via l'admin
    fields = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)