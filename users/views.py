from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .models import Profile, skill
from .models import Messages as Letters
# Create your views here.

def Profiles(request):
    users = Profile.objects.all()
    context = {
        "users":users
        }
    return render(request, "profiles.html", context)

def profile(request, id):
    user = Profile.objects.get(id=id)
    tags = user.other_skill.all()
    for tag in tags:
        tag.name = tag.name.title()
    context = {
        "user":user,
        "tags":tags
        }
    return render(request, "profile.html", context)

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "tizimga kirdingiz!")
            return redirect('profiles')
        else:
            messages.error(request, 'login va parolni xato kiritdingiz')
    if request.user.is_authenticated:
        return redirect("profiles")      
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.info(request, "tizimdan chiqdingiz")
    return redirect("profiles")

def register_user(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, "muvaffaqiyatli ro'yxatdan o'tdingiz")
            return redirect("profiles")
        else:
            messages.error(request, "formani xato to'ldirdingiz")
    form = CustomUserCreationForm()
    for f in form:
        if f.label=="Password":
            f.label="parol"
        elif f.label=="Password confirmation":
            f.label="parolni takrorlang"
    context={
        "form":form
        }
    return render(request, "register.html", context)

@login_required(login_url="login")
def my_account(request):
    profil = request.user.profile
    context = {
        "user":profil
        }
    return render(request, "account.html", context)

@login_required(login_url="login")
def profile_change(request):
    profile = request.user.profile
    if request.method=="POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    form = ProfileForm(instance = profile)
    context = {
        "form":form
        }
    return render(request, "profile_change.html", context)

@login_required(login_url="login")
def skill_add(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user.profile
            skill.save()
            return redirect("account")
    context = {
        "form":form
        }
    return render(request, "skill_add.html", context)


@login_required(login_url="login")
def skill_change(request, id):
    skil = skill.objects.get(id=id)
    if skil.user != request.user.profile:
        messages.warning(request, "Siz boshqalarning loyihalarini o'zgartira ololmaysiz!")
        return redirect("profiles")
    form = SkillForm(instance = skil)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skil)
        if form.is_valid():
            form.save()
            return redirect("account")
    context = {
        "form":form
        }
    return render(request, "skill_add.html", context)

@login_required(login_url="login")
def skill_delete(request, id):
    skil = skill.objects.get(id=id)
    if skil.user != request.user.profile:
        messages.warning(request, "Siz boshqalarning loyihalarini o'zgartira ololmaysiz!")
        return redirect("profiles")
    skil.delete()
    return redirect("account")

def message(request, id):
    profile = Profile.objects.get(id=id)
    form = MessageForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        message = form.save(commit=False)
        message.user = profile
        message.save()
        messages.info(request, "Sizning xabaringiz yuborildi")
        return redirect("profile", profile.id)
    context = {
        "form":form
        }
    return render(request, "message/message.html", context)

def message_all(request, id):
    mes = Letters.objects.filter(user = request.user.profile)
    context = {
        "info":mes
        }
    return render(request, "message/message_all.html", context)

def search_result(request):
    text = request.GET["text"]
    search_result = Profile.objects.filter(name__icontains=text)
    context = {
        "users":search_result
        }    
    return render(request, "search/search_result_user.html", context)
    
    