
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView,RetrieveAPIView
from posts.models import Post
from .serializers import PostSerializer ,UserSerializer, AuthorSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser , AllowAny
from .permissions import IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperUserOrIsStaffReadOnly
from rest_framework.viewsets import ModelViewSet







class PostViewSet(ModelViewSet):
	
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	filterset_fields = ['status', 'author__username']
	ordering_fields = ['status', 'created']
	search_fields = [
		'text',
		'author__username',
		'author__first_name',
		'author__last_name',
	]

	def get_permissions(self):
		if self.action in ['list','create']:
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAuthorOrReadOnly]
		return [permission() for permission in permission_classes]
		



class UserViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
	def get_permissions(self):
		if self.action in ['list','create']:
			permission_classes = [IsSuperUserOrIsStaffReadOnly]
		else:
			permission_classes = [IsSuperUser]
		return [permission() for permission in permission_classes]
	

class AuthorView(RetrieveAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = AuthorSerializer













