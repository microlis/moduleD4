from django.shortcuts import render

from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter
from .forms import PostForm

class PostsList(ListView):
	model = Post
	template_name = 'posts.html'
	context_object_name = 'posts'
	queryset = Post.objects.order_by('-id')
	paginate_by = 10 # постраничный вывод в 10 элементов
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
		return context

class PostDetail(DetailView):
	template_name = 'post_edit.html'
	queryset = Post.objects.all()
	
class PostCreate(CreateView):
	template_name = 'post_add.html'
	form_class = PostForm
	
class PostUpdate(UpdateView):
	template_name = 'product_add.html'
	form_class = ProductForm
	
	def get_object(self, **kwargs):
		id = self.kwargs.get('pk')
		return Post.objects.get(pk=id)
		
class PostDelete(DeleteView):
	template_name = 'post_delete.html'
	queryset = Post.objects.all()
	success_url = '/posts/'