from django.shortcuts import render, redirect
import urllib.request
import json
from .models import Name


def index(request):
    return render(request, 'home.html')


def search(request):
    if request.method == "POST":
        username = request.POST.get('username', '')

        followings = []
        followers = []
        nonfollowers = []
        user = Name(name=username)
        user.save()

        with urllib.request.urlopen("https://api.github.com/users/"+username+"/followers?per_page=100&type=owner") as url:
            data = json.loads(url.read().decode())
            for i in data:
                followers.append([i["login"], i['avatar_url']])

        with urllib.request.urlopen("https://api.github.com/users/"+username+"/following?per_page=100&type=owner") as url:
            data = json.loads(url.read().decode())
            for i in data:
                followings.append([i["login"], i['avatar_url']])

        for i in followings:
            if i not in followers:
                nonfollowers.append(i)
        return render(request, 'search.html', {'followings': followings, 'followers': followers, 'nonfollowers': nonfollowers})
    else:
        return render('/')
