from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .forms import BlogForm
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = "blog/index.html"
    
    def get_queryset(self):
        return Blog.objects.order_by("-pub_date")[:5]

class BlogCreateView(CreateView):
    form_class = BlogForm
    model = Blog
    success_url = "/"
    
    def create_post(request):
        if request.method=="POST":
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = BlogForm
        return render(request, 'blog/blog_form.html', {'form':form})

class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"
    
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content']
    template_name = "blog/update.html"
    success_url = '/'
    
    
class BlogDeleteView(DeleteView):
    model = Blog
    success_url ="/"
    