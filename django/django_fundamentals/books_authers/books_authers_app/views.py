from django.shortcuts import render, redirect
from .models import Book, Authors
# Create your views here.

def books(request):
    context={
        'all_books':Book.objects.all()
    }
    return render(request,'book.html',context)
    
def create_book(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['desc']
    )
    return redirect('/')

def book_details(request,book_id):
    context={
        'book':Book.objects.get (id=book_id),
        'all_author':Authors.objects.all()
    }
    return render(request,'book_details.html',context)

def add_author_to_book(request):
    book=Book.objects.get(id=request.POST['book_id'])
    author=Authors.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{book.id}')

def authors(request):
    context={
        'all_authors':Authors.objects.all()
    }
    return render(request,'authors.html',context)

def author_create(request):
    Authors.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')    

def author_details(request,author_id):
    context={
        'author':Authors.objects.get(id=author_id),
        'all_books':Book.objects.all()
        }
    return render(request,'author_details.html',context)

def add_book_to_author(request):
    author=Authors.objects.get(id=request.POST['author_id'])
    book=Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author.id}')

    

   

