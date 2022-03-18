from django.http import HttpResponse
from . import util
from django.shortcuts import render
from markdown2 import Markdown
import os
mkdown = Markdown()


def index(request):
    if request.method == "POST":
        query = request.POST.get('q')
        queryVar = util.get_entry(query)
        if queryVar != None:

            return render(request, "encyclopedia/query.html", {
                "query": mkdown.convert(queryVar)
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

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def query(request, query):
    return render(request, "encyclopedia/query.html", {
        "query": mkdown.convert(util.get_entry(query))
    })

def createPage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if util.get_entry(title):return HttpResponse("qwq no :p")
        newfile = open(f"entries/{title.capitalize()}.md",'w')
        content = request.POST.get('content')
        newfile.write(f"#{title.capitalize()}\n")
        newfile.write(f"{content}")
        newfile.close()
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
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
        newTitle = request.POST.get("title")
        newContent = request.POST.get("title")
        
        os.remove(f"entries/{query.capitalize()}.md")
        fileToEdit = open(f"entries/{newTitle.capitalize()}.md", "w")
        fileToEdit.write(f"#{newTitle.capitalize()}\n")
        fileToEdit.write(f"{newContent}")
        fileToEdit.close()
        return render(request, "encyclopedia/query.html", {
            "query": util.get_entry(newTitle),
            "queryName" : newTitle
        })
        
        
