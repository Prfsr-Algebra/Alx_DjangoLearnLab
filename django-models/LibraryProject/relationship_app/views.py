from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    context = {'book_list' = books}
    template = 'relationship_app/list_books.html'
    return render(request, template, context)
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    def get_object_data(self, **kwargs):
        context = super().get_object_data(**kwargs)
        book = Library.objects.all()
        context['Library_Details'] = self.objects.books.all()
        return context
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return user.userprofile.role == "Admin"

def is_librarian(user):
    return user.userprofile.role == "Librarian"

def is_member(user):
    return user.userprofile.role == "Member"

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")
from django.contrib.auth.decorators import permission_required

@permission_required("relationship_app.can_add_book")
def add_book(request):
    return HttpResponse("You have permission to add a book!")

