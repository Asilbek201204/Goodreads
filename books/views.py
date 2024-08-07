from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Comment
from django.contrib import messages
from .forms import CommentForm, BookForm
from django.contrib.auth.decorators import login_required
from django.views import View

@login_required
def books(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    if query:
        books = books.filter(title_icontains=query)
    context = {'books': books}
    return render(request=request, template_name='books.html', context=context)

@login_required
def book_detail(request, id):
    book = Book.objects.get(id=id)
    forms = CommentForm()
    context = {'book': book, 'form': forms}
    return render(request, 'book_detail.html', context)



@login_required
def book_comments(request,id):
    if request.method =='POST':
        form = CommentForm (request.POST)
        user = request.user
        book = Book.objects.get(id=id)
        if form.is_valid():
            Comment.objects.create(
                user = user,
                book = book,
                text = form.cleaned_data['text'],
                star = form.cleaned_data['star'],
            )
            messages.success(request,'Comment added successfully')
            return redirect('book_detail',id=id)
        return render(request,'book_detail', context={'book':book, 'form': form,})



@login_required
def comment_delete(request, book_id, comment_id):
    book = get_object_or_404(Book , id=book_id)
    comment = get_object_or_404(Comment, id=comment_id, book=book)
    comment.delete()
    messages.success(request, 'Comment deleted successfully')
    return redirect('book_detail', id=book_id)

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return redirect('book_detail' ,id=comment.book.id)

    return render(request, 'comment_edit.html', {'form': form, 'comment': comment})

def book_edit(request, book_id):
    # Your editing logic here
    # ...

    # Redirect to the detail view of the edited book
    return redirect('book-detail', pk=book_id)

class BookAdd(View):
    def get(self,request):
       form = BookForm()
       return render(request,'book_add.html',{'form':form}) 
        

    def post(self,request):
        form =BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Book added successfully')
            return redirect('books')
        messages.success(request,'Book is not valid')
        return render(request,'book_add.html', context={'form':form})
    


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Book

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Implement delete functionality here
    book.delete()
    messages.success(request, 'Book deleted successfully.')
    return redirect('book_list')  # Redirect to book list page

def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Process form submission for editing book
        # Example code to handle editing form submission
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book edited successfully.')
            return redirect('book_detail', book_id=book.id)  # Redirect to book detail page
    else:
        # Render form for editing book
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit_book.html', context)  # Replace with your edit book template
