from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author
from .forms import BookForm
# from .forms import SomeForms

"""
    save(), delete()

    SELECT      : all(), get()
    INSERT      : create()
    
    WHERE       : filter() (exemple : .filter(title= "Dr Slump" donne le livre dr slump...)
                    peut s utiliser ac __ , soit :
                            __gt, __lt, __gte, __lte, __startswith ...
                            greater than, lower than, great than or equal etc ...
                            exemple : .filter(quantity__gt = 10) donc quantité plus grand que 10
                                        .filter(title__startswith = "Naruto") donc tous les livres commençant par la chaine Naruto
                                        .filter(title = "Naruto") donc vérifier l'égalité, donc si c est exactement Naruto
    ORDER BY    : order_by() (order_by("title") ou order_by("-title") pour décroissant)
    LIMIT       : [:N] => récupérer les n premiers enregistrements
    
    Many-to-many : relation * -- * (tous les A et tous les B)
        donc exemple :
        book = Book.objects.get(pk = 1)
        author = Author.objects.create(name="Chuck Norris")
        book.authors.add(author)
        où "add" va ajouter cet auteur a la liste des auteurs deja existant du livre, donc on créé une relation supplémentaire
    One-to_one : 1 -- 1 revient a une requete classique mais le record est sur chaque table exemple :
        user.save()
        user_identity.save()
        
    raw() : permet d ecrire du sql dur (directement) exemple :
        "books": Book.objects.raw("SELECT * FROM mangalib_book")
        rare , uniquement qd django ne gere pas ce cas precis
"""

def index(request):
    context = {"books": Book.objects.all()}
    return render(request, "mangalib/index.html", context)
    """
    if request.method == 'POST':
        form = SomeForms(request.POST)

        if form.is_valid():
            return redirect("mangalib:index")
    else:
        form = SomeForms()

    context = {"form": form}
    return render(request, "mangalib/index.html", context)
    """

def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk=book_id)}
    return render(request, "mangalib/show.html", context)

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm()
    return render(request, "mangalib/book-form.html", {"form": form})
    """
    author = Author.objects.get(name = "Akira Toriyama")
    book = Book.objects.create(title= "Dragon Ball Z", quantity = 13, author = author)
    return redirect("mangalib:index")
    """

def edit(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm(instance=book)
    return render(request, "mangalib/book-form.html", {"form": form})
    """
    book = Book.objects.get(title= "Dragon Ball Z")
    book.title = "Dragon Ball Super"
    book.save()
    return redirect("mangalib:index")
    """

def remove(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("mangalib:index")