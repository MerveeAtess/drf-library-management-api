from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from books.serializers import AuthorSerializer, BookSerializer
from books.models import Author, Book

# vt kitapları listelemek ve vt yeni kitap kaydı ekleme;
class BookListCreateView(ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class= BookSerializer

# tekil kitaplar üzerinde(get,put,patch ve delete model)
class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer

class AuthorListCreateView(ListCreateAPIView):
    queryset= Author.objects.all()
    serializer_class= AuthorSerializer

class AuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset= Author.objects.all()
    serializer_class= AuthorSerializer





