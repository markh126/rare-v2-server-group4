from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from rareapi.models import Post, Comment, RareUser, User

class PostView(ViewSet):
    """Level up posts view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations
        
        Returns
            Response -- JSON serialized post instance
        """
        user_id = RareUser.objects.get(uid=request.data["userId"])

        post = Post.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            image_url=request.data["imageUrl"],
            user_id=user_id
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an post

        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.content = request.data["content"]
        post.publication_date = request.data["publicationDate"]
        post.image_url = request.data["imageUrl"]

        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Handle DELETE requests for single post
        
        Returns:
            Response -- Empty body with 204 status code
        """
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def add_comment(self, request, pk):
        """Post request for a user to comment on a post"""

        user_id = RareUser.objects.get(user_id=request.data["userId"])
        post = Post.objects.get(pk=pk)
        comment = Comment.objects.create(
            user_id=user_id,
            post_id=post,
            content=request.data["content"]
        )
        return Response({'message': 'Comment Added'}, status=status.HTTP_201_CREATED)

class PostSerializer(serializers.ModelSerializer):
    """JSON Serializer for posts
    """
    class Meta:
        model = Post
        fields = ('user_id', 'title', 'publication_date', 'image_url', 'content')

class CommentSerializer(serializers.ModelSerializer):
    """JSON Serializer for comments
    """
    class Meta:
        model = Comment
        fields = ('post_id', 'author_id', 'content', 'created_on')
