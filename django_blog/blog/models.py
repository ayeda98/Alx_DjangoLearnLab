from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Titre de l'article
    content = models.TextField()  # Contenu de l'article
    published_date = models.DateTimeField(auto_now_add=True)  # Date de publication (automatique)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Auteur de l'article

    def __str__(self):
        return self.title
