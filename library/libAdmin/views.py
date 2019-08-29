from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from libAdmin.models import Book
from .forms import LoginForm
from .forms import BookForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
def loginAction(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/libAdmin/welcome')
	else:	
		if request.method == 'POST':
			login_form = LoginForm(request.POST)
			if login_form.is_valid():

				username = login_form.cleaned_data['username']
				password = login_form.cleaned_data['password']

				user = authenticate(username=username, password=password)
								
				if user is not None:
					if user.is_active:
						login(request, user)	
						return HttpResponse('Login Successful')
					else:
						return HttpResponse('Your account is not active')
				else:
					return HttpResponse('The Account does not exists')
			else:
				login_form = LoginForm()
				return render(request, "login.html",{"form":login_form})
		else:
			login_form = LoginForm()
		return render(request, "login.html",{"form":login_form})

def add_Book(request):
	if request.user.is_authenticated:
    
	    if request.method == 'POST':
	        book_form = BookForm(request.POST,initial={"avail": "True"})
	        
	        if book_form.is_valid():
	            book_name = book_form.cleaned_data['book_name'] 
	            author = book_form.cleaned_data['author'] 
	            price= book_form.cleaned_data['price']
	            avail=book_form.cleaned_data['avail']
	            book_object = Book(book_name=book_name, author=author,price=price,avail=avail)
	            book_object.save() # will save the data from the form to database
	                
	            return HttpResponse('Data Inserted successfully')
	    else:
	    	book_form = BookForm()
	    	return render(request, 'addbook.html', {'form': book_form})

	else:
		return HttpResponseRedirect('/libAdmin/')


def listBooks(request):
	if request.user.is_authenticated:


		book_list = Book.objects.all()
		paginator = Paginator(book_list, 15)
		page = request.GET.get('page')
		books = paginator.get_page(page)

		return render(request, "list_books.html",{"books":books})
	else:
		return HttpResponseRedirect('/libAdmin/')

def edit_book(request,requested_id):
	print("hai")
	if request.method == 'POST':
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			book_details = Book.objects.get(id=requested_id)
			book_details.book_name = book_form.cleaned_data['book_name'] 
			book_details.author = book_form.cleaned_data['author'] 
			book_details.price= book_form.cleaned_data['price']
			book_details.avail= book_form.cleaned_data['avail']
			book_details.save()
			return HttpResponse('Data Edited successfully')

	else:
		

		book_details = Book.objects.get(id=requested_id) # this will select datafrom database 
		book_form = BookForm(initial={"book_name":book_details.book_name,"author":book_details.author,"price":book_details.price,"avail":book_details.avail,}) # this will set initial values in the form from selected data

		return render(request, 'edit_book.html', {'form': book_form,'book_id':requested_id,})	

def delete_book(request,requested_id):

	try:
		book_details = Book.objects.get(id=requested_id)  
		book_details.delete()
		book_list = Book.objects.all()
		paginator = Paginator(book_list, 15)
		page = request.GET.get('page')
		books = paginator.get_page(page)

		return render(request, "list_books.html",{"books":books})	
	except:
		return HttpResponse('The record not found!')

def welcome(request):
	messages.add_message(request, messages.INFO, 'Welcome Admin')
	return render(request, "welcome.html")