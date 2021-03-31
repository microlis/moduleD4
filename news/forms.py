from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
	
	class Meta:
		model = Post
		fields = ['head_post', 'time_in_post', 'text_post']