from . import util
from django.shortcuts import render
from markdown2 import Markdown
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

