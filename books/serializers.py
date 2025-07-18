from rest_framework import serializers
from books.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model= Author
        fields= ('id', 'name', 'bio')

class BookSerializer(serializers.ModelSerializer):
    author= serializers.PrimaryKeyRelatedField(queryset= Author.objects.all())

    class Meta:
        model= Book
        fields= ('id', 'title', 'author', 'isbn',
                  'genre', 'publication_date')
