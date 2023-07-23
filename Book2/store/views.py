from django.shortcuts import render,redirect
from django.http import *
from .forms import SignupForm,EditUser,EditUserAdmin,BookRegistration,BookForm,AuthorForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .models import Author,Book,Bookstore,Order
from django.db.models import Q

def index(request):
    return redirect("/login/")

#signup
def usersingup(request):
    print(request.POST)
    if request.method == "POST":
        form=SignupForm(request.POST)
        print("17")
        if form.is_valid():
            form.save()
            print("20")
            return redirect("/login/")
    
    else:
        print("24")
        form=SignupForm()    
    return render(request,'singup.html',{'form':form})

#login
def userlogin(request):      
        if request.method == "POST":
            form= AuthenticationForm(request=request, data=request.POST) 
            if form.is_valid():
                uname=form.cleaned_data['username']
                passw=form.cleaned_data['password']
                user=authenticate(username=uname, password=passw)
                if user is not None:
                    login(request, user)
                    messages.success(request,'lgoin successfully')
                    return HttpResponseRedirect('/book/')
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form })

#book recode
def bookdetail(request):
    if request.user.is_authenticated:
        books=Bookstore.objects.all()
        user = request.user
    else:
        return HttpResponseRedirect("/login/")
    return render(request,'book.html',{"books":books, 'user':user})


#show user detail
def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                form = EditUserAdmin(request.POST, instance=request.user)
                user = User.objects.all()
            else:
                form = EditUser(request.POST, instance=request.user)
                messages.success(request, "Update Successfully")
                form.save()
        else:
            if request.user.is_superuser:
                form = EditUserAdmin(instance=request.user)
                user = User.objects.all()
            else:
                form = EditUser(instance=request.user)
                user = None

        return render(request, 'show.html', {'name': request.user.username, 'form': form, 'user': user})
    else:
        return HttpResponseRedirect("/login/")

#logout   
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


#changepassword
def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,"Password Change successfully")
                return HttpResponseRedirect('/show/')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

#sorting
def booksort(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            sort = request.POST.get('sort')
            books=Bookstore.objects.all()
            if sort == 'price':
                books = books.order_by('price')
            elif sort == 'author':
                books = books.order_by('author_name__name')
            elif sort == 'book_name':
                books = books.order_by('book_name__bookName')

            return render(request, 'sorting.html', {'books': books})
        else:
            books = Bookstore.objects.all()
            return render(request, 'sorting.html', {'books': books})
    else:
        return HttpResponseRedirect("/login/")
    

#searching
def search(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            b_name=request.POST.get('search')
            if  b_name:
                books = Bookstore.objects.filter( Q(price__icontains= b_name) |Q(description__icontains= b_name) | Q(author_name__name__icontains= b_name) | Q(book_name__bookName__icontains= b_name))
                return render(request,'search.html',{'books':books})
        return render(request, 'search.html')
    else:
        return HttpResponseRedirect("/login/")

#pricebookauth
def addbooks(request):
    if request.user.is_authenticated:
        books = Bookstore.objects.all()
        if request.method == 'POST':
            form = BookRegistration(request.POST)
            if form.is_valid():
                form.save()
                form = BookRegistration()
                
        else:
            form = BookRegistration()
        return render(request,'add.html', {"form":form, "books":books })
    else:
        return HttpResponseRedirect("/login/")


#addbook
def addbookauth(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['bookName']
            
            if Book.objects.filter(bookName=book_name).exists():
                messages.error(request, "Book already exists.")
                return redirect('/addauth/')
            else:
                form.save()
                form = BookForm()
                messages.success(request, "Book add successfully.")
                return redirect('/addauth/')
                
    else:
        form = BookForm()

    return render(request, 'addbookauth.html', {'form': form})

#addauthor
def addauthor(request):
        if request.method == 'POST':
            form = AuthorForm(request.POST)
            if form.is_valid() :
                authorname=form.cleaned_data['name']

                if Author.objects.filter(name=authorname).exists():
                    messages.error(request, "Author already exists.")
                    return redirect('/adddata/')
                else:
                    form.save()
                    form = AuthorForm()
                    messages.success(request, "Author add successfully.")
                    return redirect('/adddata/')
        else:
            form = AuthorForm()
        return render(request, 'addauth.html', {"form": form})

#bookdelet
def delete(request, id):
    if request.method == 'POST':
        delt = Bookstore.objects.get(pk=id)
        delt.delete()
        return redirect('/adddata/')

def update(request,id):
    if request.method=="POST":
        books=Bookstore.objects.get(pk=id)
        form=BookRegistration(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect("/adddata/")
    else:
        books=Bookstore.objects.get(pk=id)
        form=BookRegistration(instance=books)
    return render(request,'update.html',{"form":form})


#buybook
def buy(request, id):
    if request.method == "POST":
        book = Bookstore.objects.get(pk=id)
        books = book.book_name
        user = request.user
        orders = Order(book=books, bookPrice=book.price ,customername=user)
        orders.save()
        return redirect("book")  

    orders = Order.objects.all()
    user = User.objects.all()

    return render(request, 'cart.html', {"orders": orders, "user": user})


def afterbuy(request):
    orders = Order.objects.filter(customername=request.user)
    return render(request, 'cart.html', {"orders": orders})
  
 
def deletecart(request, id):
    if request.method == 'POST':
        if Order.objects.filter(pk=id).exists():
            order = Order.objects.get(pk=id)
            order.delete()
            return redirect('/buy/')
        else:
            return HttpResponse('Please enter book in cart')
        




