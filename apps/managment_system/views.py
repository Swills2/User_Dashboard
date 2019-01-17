from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def registerpage(request):
    return render(request, 'register.html')


def register(request):
    form = request.POST
    has_errors = False

    if len(form['first_name']) < 3:
        has_errors = True
        messages.error(request, 'First name must be at least 3 characters.')
    if len(form['last_name']) < 3:
        has_errors = True
        messages.error(request, 'Last name must be at least 3 characters.')
    if len(form['email']) < 8:
        has_errors = True
        messages.error(request, 'Email must be at least 8 characters.')
    if len(form['password']) < 8:
        has_errors = True
        messages.error(request, 'Password must be at least 8 characters.')
    if not form['password'] == form['password_confirmation']:
        has_errors = True
        messages.error(request, 'Password and password confirmation do not match')

    if has_errors:
        return redirect('/register_page')

    try:
        user = User.objects.get(email=form['email'])
        messages.error(request, 'User with this email exists. Please login.')
        return redirect('/register_page')

    except User.DoesNotExist:
        hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        normal_hashed_pw = hashed_pw.decode('utf-8')
        user = User.objects.create(
            first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=normal_hashed_pw)

        messages.success(request, "You succesfully registered. Please login.")

    return redirect('/login_page')


def loginpage(request):
    return render(request, 'signin.html')


def login(request):
    form = request.POST
    try:
        user = User.objects.get(email=form['email'])

    except User.DoesNotExist:
        messages.error(
            request, 'User with this email does not exist please register.')
        return redirect('/login_page')

    password_correct = bcrypt.checkpw(
        form['password'].encode(), user.password.encode())

    if not password_correct:
        messages.error(request, 'Email/password does not match.')
        return redirect('/login_page')

    else:

        request.session['user_id'] = user.id
        if user.id == 1:
            user.is_admin = True
            user.save()

        return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')


def dashboard(request):
    if not 'user_id' in request.session:
        messages.error(
            request, 'Your need to login to be able to view this page.')
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.all()

    context = {
        'user': user,
        'users': users,
    }

    return render(request, 'dashboard.html', context)


def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/dashboard')


def adduser(request):
    if not 'user_id' in request.session:
        messages.error(
            request, 'You need to login to be able to view this page.')
        return redirect('/')

    return render(request, 'addnew.html')


def newuser(request):
    form = request.POST
    error = []

    if len(form['first_name']) < 3:
        has_errors = True
        messages.error(request, 'First name must be at least 3 characters.')
    if len(form['last_name']) < 3:
        has_errors = True
        messages.error(request, 'Last name must be at least 3 characters.')
    if len(form['email']) < 8:
        has_errors = True
        messages.error(request, 'Email must be at least 8 characters.')
    if len(form['password']) < 8:
        has_errors = True
        messages.error(request, 'Password must be at least 8 characters.')
    if not form['password'] == form['password_confirmation']:
        has_errors = True
        messages.error(
            request, 'Password and password confirmation do not match')

        if has_errors:
            return redirect('/adduser')

    try:
        user = User.objects.get(email=form['email'])
        messages.error(request, 'User with this email exists. Please login.')
        return redirect('/adduser')

    except User.DoesNotExist:
        hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        normal_hashed_pw = hashed_pw.decode('utf-8')
        user = User.objects.create(
            first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=normal_hashed_pw)

        messages.success(request, "You succesfully registered. Please login.")

    return redirect('/dashboard')


def edit(request, user_id):
    if not 'user_id' in request.session:
        messages.error(request, 'You need to login to be able to view this page.')
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])

    context = {
        'user': user, 
    }
    return render(request, 'edit.html', context)


def nameupdate(request, user_id):
    user = User.objects.get(id=user_id)
    form = request.POST
    error = []

    if not 'user_id' in request.session:
        messages.error(
            request, 'You need to login to be able to view this page.')
        return redirect('/')

    if len(form['first_name']) < 3:
        has_errors = True
        messages.error(request, 'First name must be at least 3 characters.')
    if len(form['last_name']) < 3:
        has_errors = True
        messages.error(request, 'Last name must be at least 3 characters.')
    if len(form['email']) < 8:
        has_errors = True
        messages.error(request, 'Email must be at least 8 characters.')

    else:
        user.first_name = form['first_name']
        user.last_name = form['last_name']
        user.email = form['email']
        user.save()

    return redirect('/dashboard')

def descupdate(request, user_id):
    user = User.objects.get(id=user_id)
    form = request.POST
    error = []

    if not 'user_id' in request.session:
        messages.error(
            request, 'You need to login to be able to view this page.')
        return redirect('/')
    
    if len(form['description']) < 3:
        has_errors = True
        messages.error(request, 'Description must be at least 3 characters.')

    else:
        user.description = form['description']
        user.save()

    return redirect('/dashboard')

def view(request, user_id):
    if not 'user_id' in request.session:
        messages.error(request, 'You need to login to be able to view this page.')
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    users = User.objects.get(id=user_id)

    context = {
        'user': user,
        'users': users,
        'post_data':Message.objects.all(),
        'comment_data':Comment.objects.all(),
    }

    return render(request, 'view.html', context)

def add_message(request):
    Message.objects.create(message=request.POST['add_message'], user=User.objects.get(id=request.session['user_id']))
    messages.success(request,'Message posted successfully.')
    print(Message.objects.get(id=1))
    return redirect('/dashboard')    


def comment(request):
    Comment.objects.create(comment=request.POST['comment'],user=User.objects.get(id=request.session['user_id']),message=Message.objects.get(id=request.POST['message_ID']) )
    return redirect('/dashboard')

def delete_message(request, message_id):
    m = Message.objects.get(id=message_id)
    m.delete()
    return redirect('/dashboard')  