from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostView, Comment, Like


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    )


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    )


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
