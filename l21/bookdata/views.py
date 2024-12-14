from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book
from django.db.models import Count


# Create your views here.
def all_view(request):
    if request.method == "GET":

        # prefetch books with authors
        books = Book.objects.prefetch_related('author')

        # Make a list of all the books and authors from prefetch_related
        data = [[book.title, book.author.first_name] for book in books]

        return render(request, "listData.html", {"data":data})
    else:
        return HttpResponse("Bad request.", status=400)

def top_3_view(request):
    if request.method == "GET":

        # Get the authors with book count in it.
        authors = Author.objects.annotate(book_count=Count('books'))

        data = [[author.first_name, author.book_count] for author in authors]

        # this sorts the 2d array by the second number which is the book count
        sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

        # This makes sure we get either top 3 or (if we have less than 3) the count of all the authors
        top = min(3, Author.objects.count())

        # Get top 3 from array
        top_3 = sorted_data[0:3]

        return render(request, "listData.html", {"data": top_3})
    else:
        return HttpResponse("Bad request.", status=400)

def classics_view(request):
    if request.method == "GET":

        # Get only the books that released before 200
        books = Book.objects.filter(release_year__lt=2000)

        data = [book.title for book in books]

        return render(request, "listData.html", {"data": data})
    else:
        return HttpResponse("Bad request.", status=400)