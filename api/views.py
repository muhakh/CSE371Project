from rest_framework import generics
from ..models.comment import DocumentComment, PageComment
from .serializers import DocumentCommentSerializer ,PageCommentSerializer
from rest_framework.permissions import IsAuthenticated

class PageCommentListView(generics.ListAPIView):
    queryset = PageComment.objects.all()
    serializer_class = PageCommentSerializer

class PageCommentDetailView(generics.RetrieveAPIView):
    queryset = PageComment.objects.all()
    serializer_class = PageCommentSerializer

class PageCommentCreateView(generics.ListCreateAPIView):
    queryset = PageComment.objects.all()
    serializer_class = PageCommentSerializer
    permission_classes = (IsAuthenticated,)

class DocumentCommentListView(generics.ListAPIView):
    queryset = DocumentComment.objects.all()
    serializer_class = DocumentCommentSerializer

class DocumentCommentDetailView(generics.RetrieveAPIView):
    queryset = DocumentComment.objects.all()
    serializer_class = DocumentCommentSerializer

class DocumentCommentCreateView(generics.ListCreateAPIView):
    queryset = DocumentComment.objects.all()
    serializer_class = DocumentCommentSerializer
    permission_classes = (IsAuthenticated,)
