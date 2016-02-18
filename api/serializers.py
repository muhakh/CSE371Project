from rest_framework import serializers
from ..models.comment import DocumentComment, PageComment

class PageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageComment
        fields = ('id', 'content', 'page', 'owner')

class DocumentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentComment
        fields = ('id', 'content', 'document', 'owner')
