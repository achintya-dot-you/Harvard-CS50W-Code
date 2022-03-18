from django.http import HttpResponse
from . import util
from django.shortcuts import render
from markdown2 import Markdown
import os
import random
mkdown = Markdown()


def index(request):
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def query(request, query):
    queryDup = util.get_entry(query)
    print(queryDup)
    if queryDup!=None:
        queryMarkdown = mkdown.convert(queryDup)
        return render(request, "encyclopedia/query.html", {
            "query": queryMarkdown,
            "queryName" : query.capitalize()
        })
    else:
        return render(request, "encyclopedia/404error.html")

def createPage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if util.get_entry(title):return HttpResponse(f"An entry already exists with the name '{title.capitalize()}' <br> Do you want to <a href='edit/{title.capitalize()}'>edit it</a> instead?")
        newfile = open(f"entries/{title.capitalize()}.md",'w')
        content = request.POST.get('content')
        newfile.write(f"{content}")
        newfile.close()
        return render(request, "encyclopedia/query.html", {
            "query": mkdown.convert(util.get_entry(title)),
            "queryName": title.capitalize()
        })
    return render(request, "encyclopedia/newpage.html")

def editPage(request, query):
    if request.method == "GET":
        queryName = util.get_entry(query)
        print(query)
        if query != None:
            return render(request, "encyclopedia/editpage.html",{
                "query" : queryName,
                "queryName" : query.capitalize()
            })
    else:
        newContent = request.POST.get("content")
        print(newContent)
        os.remove(f"entries/{query.capitalize()}.md")
        fileToEdit = open(f"entries/{query.capitalize()}.md", "w")
        fileToEdit.write(f"{newContent}")
        fileToEdit.close()
        return render(request, "encyclopedia/query.html", {
            "query": mkdown.convert(util.get_entry(query.capitalize())),
            "queryName" : query.capitalize()
        })

def randomPage(request):
    entries = []
    for entry in util.list_entries():
        entries.append(entry)
    
    randomEntry = random.choice(entries)

    return render(request, f"encyclopedia/query.html", {
        "query" : mkdown.convert(util.get_entry(randomEntry)),
        "queryName" : randomEntry.capitalize()
    })    
        
def search(request):
    if request.method=="POST":
        query = request.POST.get('q')
        queryVar = util.get_entry(query)
        if queryVar != None:

            return render(request, "encyclopedia/query.html", {
                "query": mkdown.convert(queryVar),
                "queryName": query.capitalize()
            })
        else:
            entries = []
            for entry in util.list_entries():
                if query.lower() in entry.lower():
                    entries.append(entry)
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "entries": entries
            })
