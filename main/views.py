from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # return HttpResponse("<h1>Hello World! %s </h1>" %id)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            #n = form.cleaned_data['name']
            #print("cleaned name ", n)
            #print("cleaned check ", form.cleaned_data['check'])
            #print("cleaned all ", form.cleaned_data)
            t = ToDoList(name=form.cleaned_data['name'])
            t.save()

    else:
        form = CreateNewList()
    
    return render(response, "main/create.html", {"form": form})
