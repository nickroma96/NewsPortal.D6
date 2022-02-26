from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter
from datetime import datetime
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/post.html'
    queryset = Post.objects.all()


class PostSearch(PostList):
    template_name = 'flatpages/search.html'
    context_object_name = 'search'
    filter_class = PostFilter

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs


class PostCreate(CreateView):
    template_name = 'flatpages/add.html'
    form_class = PostForm


class PostUpdate(UpdateView):
    template_name = 'flatpages/edit.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDelete(DeleteView):
    template_name = 'flatpages/delete.html'
    queryset = Post.objects.all()
    success_url = '/news/delete/'