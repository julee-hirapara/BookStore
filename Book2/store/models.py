from django.db import models
from django import forms


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    bookName = models.CharField(max_length=100)
    authorName= models.ManyToManyField(Author, through='Bookstore')

    def __str__(self):
        return self.bookName

class Bookstore(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.book_name.bookName
    
class Order(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    customername = models.CharField(max_length=100)
    bookPrice=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.book.bookName

