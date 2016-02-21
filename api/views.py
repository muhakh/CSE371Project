from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from ..models.comment import DocumentComment, PageComment
from .serializers import DocumentCommentSerializer ,PageCommentSerializer
from rest_framework.permissions import IsAuthenticated

class PageCommentListView(generics.ListAPIView):
    def get_queryset(self):
        page_id = self.kwargs['pk']
        return PageComment.objects.filter(page=page_id)
    serializer_class = PageCommentSerializer

class PageCommentCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        page_id = self.kwargs['pk']
        return PageComment.objects.filter(page=page_id)
    serializer_class = PageCommentSerializer
    permission_classes = (IsAuthenticated,)

class DocumentCommentListView(generics.ListAPIView):
    def get_queryset(self):
        doc_id = self.kwargs['pk']
        return DocumentComment.objects.filter(document=doc_id)
    serializer_class = DocumentCommentSerializer

class DocumentCommentDetailView(generics.RetrieveAPIView):
    def get_queryset(self):
        doc_id = self.kwargs['pk']
        return DocumentComment.objects.filter(document=doc_id)
    serializer_class = DocumentCommentSerializer

class DocumentCommentCreateView(generics.ListCreateAPIView):
    def get_queryset(self):
        doc_id = self.kwargs['pk']
        return DocumentComment.objects.filter(document=doc_id)
    serializer_class = DocumentCommentSerializer
    permission_classes = (IsAuthenticated,)
