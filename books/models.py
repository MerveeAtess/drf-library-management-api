from django.db import models

# kitapların ve bu kitapların yazarlarını temsil eden modellerin tanımlaması;
class Author(models.Model):
    name= models.CharField(max_length=200)
   
    # tercihen girilebilir
    bio= models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title= models.CharField(max_length=250)
    
    # many to many ilişki 
    author= models.ForeignKey(Author, on_delete=models.CASCADE,
                              related_name='books')
    
    # kitap doğrulama sistemi - çakışma olmamalı!
    isbn= models.CharField(max_length=13, unique=True)
    genre= models.CharField(max_length=250)

    publication_date= models.DateField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"

