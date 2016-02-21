from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.page import Page

class PageDetail(LoginRequiredMixin, DetailView):
    model = Page
    template_name='page/detail.html'
