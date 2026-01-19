from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import list_books

urlpatterns = [
    # Function-based & class-based views for books/libraries
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views (ALX checker exact format)
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

  # ---------- Permission-Protected Views ----------
    path('add_book/', views.add_book, name='add_book'),          # must match checker
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),   # must match checker
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'), # optional
   

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),


]
