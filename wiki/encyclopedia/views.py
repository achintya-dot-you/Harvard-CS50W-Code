from django.shortcuts import render
from markdown2 import Markdown
mkdown = Markdown()
from . import util


def index(request):
    if request.method == "POST":
        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def query(request, query):
    code = mkdown.convert(util.get_entry(query))
    print(code)
    return render(request, "encyclopedia/query.html", {
        "query" : code
    })

