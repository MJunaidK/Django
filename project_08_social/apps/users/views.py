import profile
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.posts.models import Post
from .models import Profile

from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('User logged in successfully')
            else:
                return HttpResponse('Invalid login credentials')
    else:    
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.get(user=current_user)    
    return render(request, 'users/index.html', {'posts': posts, 'profile': profile})


def register(request):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                Profile.objects.create(user=new_user)
                # Profile.objects.create(user=new_user) # One step creation
                # profile = Profile(user=new_user)  # Step 1: create instance
                # profile.save()                    # Step 2: save to DB
                return render(request, 'users/register_done.html')
        else:
            user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        # The ModelForm metaclass of UserEditForm does something like this
        # 1. Read Meta.model → User
        # 2. Read Meta.fields → ['email', 'first_name', 'last_name']
        # 3. Look at the User model’s fields
        # 4. Auto‑generate form fields for each one
        # 5. Build a save() method that updates a User instance
        # 6. Build validation rules based on the model
        # hence it knows the instance is of User type
        user_form = UserEditForm(instance=request.user, data=request.POST)
       
          # The ModelForm metaclass of ProfileEditForm does something like this
          # 1. data=request.POST -> Bind normal form data
          # 2. files=request.FILES -> Bind uploaded files
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        # currently logged in instance of User
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })