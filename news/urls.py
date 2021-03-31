from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
	
	path('', PostsList.as_view()),
	path('<int:pk>', PostDetail.as_view(), name='post_edit'),
	path('add/', ProductCreate.as_view(), name='post_add'),
	
]