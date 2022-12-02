import random

from django.shortcuts import render, redirect
from .forms import SearchForm, NewPage
from . import util
from django.contrib import messages
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "title": "Encyclopedia",
        "entries": util.list_entries(),
        "search_form": SearchForm

    })


def show(request, title):
    entries = util.list_entries()
    if title in entries:
        return render(request, "encyclopedia/content.html", {
            "entry": markdown2.markdown(util.get_entry(title)),
            "title": title,
            "search_form": SearchForm

        })
    else:
        return render(request, "encyclopedia/error.html", {
            "message": f"The page with name {title} does not exist in encyclopedia!",
            "search_form": SearchForm

        }, None, 404)


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        q = form.cleaned_data['q']
        entries = util.list_entries()
        entries_starts_with_given_title = [word for word in entries if word.startswith(q)]

        if len(entries_starts_with_given_title) > 1:
            return render(request, "encyclopedia/index.html", {
                "entries": entries_starts_with_given_title,
                "title": "Search result",
                "search_form": SearchForm
            })
        else:
            return redirect('show', title=q)


def create_new_page(request):
    if request.method == 'POST':
        entries = util.list_entries()
        create_form = NewPage(request.POST)
        if create_form.is_valid():
            title = create_form.cleaned_data['title']
            content = create_form.cleaned_data['content']
            if title in entries:
                messages.error(request, "Document already exist")
                return redirect('new_page')
            else:
                util.save_entry(title, content)
                return redirect('show', title=title)
    elif request.method == 'GET':
        return render(request, "encyclopedia/new_page.html", {
            "title": "Create New Page",
            "create_form": NewPage,
            "search_form": SearchForm
        })


def rand_choose(request):
    entries = util.list_entries()
    title = random.choice(entries)
    return redirect('show', title=title)
