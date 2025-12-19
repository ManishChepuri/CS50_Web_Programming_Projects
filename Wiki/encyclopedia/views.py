from django.shortcuts import render, redirect
from django import forms
from . import util
import markdown2
import random

class NewTaskForm(forms.Form):
    wiki_page = forms.CharField(label="Search Encyclopedia")


def index(request):
    if request.GET.get("random") == "true":
        rand_title = random.choice(util.list_entries())
        return redirect("encyclopedia:entry", title=rand_title)
    form = NewTaskForm(request.GET)
    if form.is_bound and form.is_valid():
        query = form.cleaned_data["wiki_page"]
        return redirect("encyclopedia:entry", title=query)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": NewTaskForm(),
    })

def entry(request, title):
    contents = util.get_entry(title)
    if contents is None:
        results = [entry for entry in util.list_entries() if title in entry]
        if len(results) != 0:
            return render(request, "encyclopedia/search.html", {
                "results": results,
                "title": title
            })
        return render(request, "encyclopedia/error.html", {
                "error_message": f'"{title.strip()}" does not exist.'
            })

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "contents": markdown2.markdown(contents.strip()),
    })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title in util.list_entries():
            return render(request, "encyclopedia/error.html", {
                "error_message": f'"{title.strip()}" already exists.'
            })
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("encyclopedia:entry", title=title)
    return render(request, "encyclopedia/new_page.html")

def edit_page(request, title):
    if request.method == "POST":
        new_content = request.POST.get("new_content")
        util.save_entry(title, new_content)
        return redirect("encyclopedia:entry", title=title)

    if title not in util.list_entries():
        return render(request, "encyclopedia/error.html", {
                "error_message": f'"{title.strip()}" does not exist.'
            })
    return render(request, "encyclopedia/edit_page.html", {
        "title": title,
        "content": util.get_entry(title)
    })
