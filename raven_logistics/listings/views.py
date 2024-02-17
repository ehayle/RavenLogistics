# listings/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from listings.models import Post, Comment
from listings.forms import CommentForm

def listings_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "listings/index.html", context)

def listings_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "listings/category.html", context)    

def listings_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                location=form.cleaned_data["location"],
                phone=form.cleaned_data["phone"],
                email=form.cleaned_data["email"],
                certifications=form.cleaned_data["certifications"],
                availability=form.cleaned_data["availability"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
        
    }

    return render(request, "listings/detail.html", context)