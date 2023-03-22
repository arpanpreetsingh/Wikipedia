from django.shortcuts import render
import markdown2
from . import util
from django.http import HttpResponse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# function to open a page for the entry the user searched for 

def entry(request, pk):
	entry = util.get_entry(pk)
	if entry == None:
		return HttpResponse("<p>Entry Not Found</p>")
	else:
		html = markdown2.markdown(entry)

		return render(request, "encyclopedia/entry.html", {
			"title_entry" : pk,
			"html_content": html
		})

