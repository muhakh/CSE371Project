from rest_framework import serializers
from ..models.comment import DocumentComment, PageComment

class PageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageComment
        fields = ('content', 'page', 'owner')

class DocumentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentComment
        fields = ('content', 'document', 'owner')
