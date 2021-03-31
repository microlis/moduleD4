from django_filters import FilterSet
from .models import Post
 
 
# создаём фильтр
class PostFilter(FilterSet):
	class Meta:
		model = Post
		fields = {'time_in_post': ['gt'],  'head_post': ['icontains'],  'author': ['icontains'],  }