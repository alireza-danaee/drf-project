from rest_framework import serializers 
from posts.models import Post
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id" , "username" , "first_name" , "last_name"]




class PostSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedIdentityField(view_name='api:author-detail')
    class Meta:
        model = Post
        fields = "__all__"

    def validate_text(self, value):
        filter_list = ["hello" , "ali" , "danaee"]

        for i in filter_list:
            if value == i:
                raise serializers.ValidationError(f"Bad Word : {i}")
        
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"




        