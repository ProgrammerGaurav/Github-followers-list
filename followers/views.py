from django.shortcuts import render, redirect
import urllib.request
import json


def index(request):
    return render(request, 'home.html')


def search(request):
    if request.method == "POST":
        link = request.POST.get('link', '')

        followings = []
        followers = []
        nonfollowers = []

        my_string = str(link)
        username = my_string.split("com/", 1)[1]

        with urllib.request.urlopen("https://api.github.com/users/"+username+"/followers") as url:
            data = json.loads(url.read().decode())
            for i in data:
                followers.append([i["login"], i['avatar_url']])

        with urllib.request.urlopen("https://api.github.com/users/"+username+"/following") as url:
            data = json.loads(url.read().decode())
            for i in data:
                followings.append([i["login"], i['avatar_url']])

        for i in followings:
            if i not in followers:
                nonfollowers.append(i)
        return render(request, 'search.html', {'followings': followings, 'followers': followers, 'nonfollowers': nonfollowers})
    else:
        return render('/')
