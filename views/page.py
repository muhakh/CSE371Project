from django.views.generic import ListView , DetailView
from ..models.page import Page

class PageDetail(DetailView):
    model=Page
    template_name='page/detail.html'
