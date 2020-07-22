from django.shortcuts import render, HttpResponseRedirect
from .models import Post, UserContact
from .forms import SignUpForm, LoginForm, PostForm,UserContactForm, UserProfileForm, PasswordChangeCustomForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import Group, User
# from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'home': 'active'})

# About
def about(request):
    return render(request, 'blog/about.html', {'about': 'active'})

# Contact
def contact(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            desc = form.cleaned_data['desc']
            client = UserContact(name=name, email=email, phone=phone, desc=desc)
            client.save()
            form = UserContactForm()
            messages.success(request, 'Thanks! We will be contact you soon.')
    else:
        form = UserContactForm()
    return render(request, 'blog/contact.html', {'contact': 'active', 'form': form})

# Dashboard
def dashboard(request):
    posts = Post.objects.all()
    user = request.user
    fullname = user.get_full_name()
    gps = user.groups.all()
    return render(request, 'blog/dashboard.html', {'dashboard': 'active', 'posts': posts, 'fullname': fullname, 'groups': gps})

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have Loggedin Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form, 'login': 'active'})
    else:
        return HttpResponseRedirect('/dashboard/')

# Singup
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! You become an Author & Registration Successfully!')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form, 'signup': 'active'})

#add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Post Added Successfull!!')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')

#Update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

# Delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# user profile
def user_profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        return render(request, 'blog/userprofile.html', {'user': user})
    else:
        return HttpResponseRedirect('/login/')

#user details
def user_detail(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Your Details Update Successfully!!')
                form.save()
                return render(request, 'blog/userprofile.html')
        else:
            form = UserProfileForm(instance=request.user)
        return render(request, 'blog/editprofile.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/',)

#change password
def change_password(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeCustomForm(
                user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(
                    request, 'Your Password Changed Suceessfully!!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = PasswordChangeCustomForm(request.user)
        return render(request, 'blog/changepassword.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
